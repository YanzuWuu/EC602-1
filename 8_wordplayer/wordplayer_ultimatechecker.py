""" EC602 Fall 2017

wordplayer checker for python and C++

"""

from subprocess import PIPE,Popen,run
import time
import os
import urllib.request
import random
import sys
from io import StringIO
import logging
import hashlib

try:
    import ec602lib
except Exception as e:
	print(e)
	quit()

try:
    assert ec602lib.VERSION >= (2,2)
except:
    print('please download the updated ec602lib.py before continuing')
    quit()


Tests_680=[
('pealp 5',['apple']),
('panesrinse 5',['apers', 'apres', 'aspen', 'asper', 'napes', 'neaps', 'panes', 'pares', 'parse', 'peans', 'pears', 'peris', 'piers', 'prase', 'presa', 'pries', 'prise', 'reaps', 'reins', 'resin', 'rinse', 'ripes', 'risen', 'serin', 'siren', 'sneap', 'spare', 'spean', 'spear', 'speir', 'spier', 'spire']),
('optsrase 5',['apers', 'apres', 'asper', 'pares', 'parse', 'paste', 'pates', 'pears', 'peats', 'prase', 'presa', 'reaps', 'septa', 'spare', 'spate', 'spear', 'tapes', 'tepas']),
('optsrase 4', ['ares', 'ates', 'ears', 'east', 'eats', 'eras', 'etas', 'opts', 'post', 'pots', 'rase', 'sate', 'sear', 'seat', 'sera', 'seta', 'spot', 'stop', 'teas', 'tops']),
('optsrase 3',[]),
('helicopter 9',[]),
]

Tests_100k=[
('anechocixq 8',['anechoic']),
('hemangiomatacountermarch 17',[]),
('midwintersaxe 9',['anxieties', 'dementias', 'dreamiest', 'examiners', 'mediatrix', 'meridians', 
    'midwinter', 'tradesmen', 'waterside']),
('on 2',['no','on']),
('act 3',['act', 'cat']),
('apoplecticmacabre 6',(226,'f63890384aba76bd150a0eb6851fea2c91f0a62e4eaf51ac7b8958275fdb74d7')),
('psychohistoriannoncollector 8',(1153,'277ac94d3d2d3673696d739284d55581cdc58be34dd56aee924070849a0e56d8')),
('apoplecticmacabre 5',(241,"f19de8e40265464b224f7c2b59db4ce9f2a19d8f73c6558ef4a25f74961347c3")),
('anechocixq 8',['anechoic']),
('punishableanglerfishes 10',(116,"8414f89b71b4383366956674155a9b21efb30fee5c400d5f6f3f5fe5fc7b8d10")),
('psychohistoriannoncollector 15',['anthropocentric', 'ethnohistorians', 'interscholastic', 'introspectional', 'neocolonialists', 
                                   'prehistorically', 'synchronisation', 'thyrocalcitonin']),
]

Tests_Speed = [
({'cpp':0.000105,'py':0.0001388},'on 2',['no','on'],),
({'cpp':6.57e-05,'py':0.000064},'act 3',['act', 'cat']),
({'cpp':0.00164,'py':0.01077},'apoplecticmacabre 5',(241, 'f19de8e40265464b224f7c2b59db4ce9f2a19d8f73c6558ef4a25f74961347c3')),
({'cpp':0.000071,'py':0.000102},'anechocixq 8',['anechoic']),
({'cpp':0.00313,'py':0.0293},'psychohistoriannoncollector 8',(1153, '277ac94d3d2d3673696d739284d55581cdc58be34dd56aee924070849a0e56d8')),
({'cpp':0.00118,'py':0.0198},'punishableanglerfishes 10',(116, '8414f89b71b4383366956674155a9b21efb30fee5c400d5f6f3f5fe5fc7b8d10')),
({'cpp':0.000188,'py':0.00274},'psychohistoriannoncollector 15',(8, 'e3f648151b3790d7f0e0f73f65c03d261d8d2c5c64b09094184e26d316c10424')),
]




def ask_wordplayer(process,case):
    process.stdin.write(case+'\n')
    process.stdin.flush()
    words = []
    while True:
        res=process.stdout.readline()
        if res=='.\n':
            break
        else:
            words.append(res.strip())
    return words

def check(answer,words,case):
    res=""
    if type(answer)==tuple:
        h = hashlib.sha256()
        h.update("".join(words).encode())
        key = (len(words),h.hexdigest())
        if key != answer:
            res += "Case {}: hex digests do not match: {} vs {}.\n".format(case,key,answer)
    elif words != answer:
        res += "Case {}: correct: {}, yours: {}\n".format(case,answer,words)
    return res

def wordplayer_tester(program_name,word_list_name,Tests):
        args = ['python'] if program_name.endswith('py') else []
        args += [program_name,word_list_name]
        popen_specs={'stdout':PIPE,'stdin':PIPE,'universal_newlines':True}

        process = Popen(args,**popen_specs)
        time.sleep(0.02)
        return_code = process.poll()
        if return_code:
            return False,'Your program exited with return code {}.'.format(return_code)

        res = ""
        for case,answer in Tests:
            res += check(answer, ask_wordplayer(process,case), case)

        if res:
            return False, res

        (stdout, stderr) = process.communicate('stopthisprogramrightnowplease 0\n',timeout=1)
        if stdout != "":
            return False, "Responding to exit signal"
        elif stderr != None:
            return False, "Extra output to stderr."

        return True,"all tests passed"

       
def test_speed(program_name,faster_than_server,fh):
        testtype = 'py' if program_name.endswith('py') else "cpp"
        args = ['python'] if program_name.endswith('py') else []
        args += [program_name,'words100k.txt']
        popen_specs={'stdout':PIPE,'stdin':PIPE,'universal_newlines':True}

        process = Popen(args,**popen_specs)


        time.sleep(0.02)
        if process.poll():
            print('aborting speed test. program not alive.')
            return {}

        time.sleep( (2 if testtype=="py" else 0.4) / faster_than_server)
        speed_factor=[]
        for target_time, case, answer in Tests_Speed:
                durations = []
                for test in range(3):
                    start_time=time.time()
                    words = ask_wordplayer(process,case)
                    durations.append((time.time()-start_time) * faster_than_server)

                speed_factor.append((case, sum(durations)/3, target_time[testtype]))
                result = check(answer, words, case)
                if result:
                    print('aborting speed test due to error in output.')
                    print(result)
                    return {}


        print('Speed test results',file=fh)
        print('==================',file=fh)
        print('Your Time    Our Time    Ratio   Case',file=fh)
        print('---------    --------    -----   ----',file=fh)
        for test,your_time,target_time in speed_factor:
            print("{:>8.4f}ms {:>8.4f}ms {:>8.3f}".format(your_time*1000,target_time*1000,your_time/target_time),test,file=fh)
        print(file=fh)
        
        scores = tuple(x[1]/x[2] for x in speed_factor)
        try:
                (stdout, stderr) = process.communicate('stopthisprogramrightnowplease 0\n',timeout=1)
        except:
            return {}

        return sorted(scores)





def main_python(program_to_run,original_name,faster_than_server,save=False):

    fh = StringIO() if save else sys.stdout

    print('Checking {} for EC602 submission.\n'.format(original_name),file=fh)

    Grade={'specs':0,'style':0,'elegance':0,'efficiency':0}

    s1=time.time()
    the_program = ec602lib.read_file(program_to_run)
    authors = ec602lib.get_authors(the_program, 'py')
    imported = ec602lib.get_python_imports(the_program)
    logging.info('init %f',time.time()-s1)
 
    s1=time.time()
    passed_short, short_report = wordplayer_tester(program_to_run,'words680.txt',Tests_680)
    if not passed_short:
        print(short_report,file=fh)
    logging.info('short %f',time.time()-s1)

    s1=time.time()
    passed_big, big_report = wordplayer_tester(program_to_run,'words100k.txt',Tests_100k)
    if not passed_big:
        print(big_report,file=fh)
    
    logging.info('big %f',time.time()-s1)

    if not passed_big or not passed_short:
        if save:
            return Grade,fh.getvalue()
        return

    s1=time.time()
    pep8_errors,pep8_report = ec602lib.pep8_check(program_to_run)
    logging.info('pep8 %f',time.time()-s1)

    s1=time.time()
    pylint_score,pylint_report = ec602lib.pylint_check(program_to_run)
    logging.info('pylint %f',time.time()-s1)
    

    s1=time.time()
    code_metrics = ec602lib.code_analysis_py(the_program)
    logging.info('analysis %f',time.time()-s1)

    complexity = code_metrics['lines']+code_metrics['words'] + 20*code_metrics['words']/code_metrics['lines']

    s1=time.time()
    rel_times = test_speed(program_to_run,faster_than_server,fh)
    logging.info('speed %f',time.time()-s1)

    eff_grade = []
    for ratio,scale in zip(rel_times,[0.5,0.2,0.1,0.05,0.05,0.05,0.05]):
        eff_grade.append(scale / ratio)


    Grade['specs']=3
    Grade['style']=max(0,(10-pep8_errors)/20) + pylint_score/20

    Grade['elegance'] = min(1.5,300/complexity) # 0.5 bonus point possible
    Grade['efficiency'] = min(2.0,sum(eff_grade)) # 1.0 bonus point possible

    print('---- analysis of your code structure ----\n',file=fh)

    print('authors          : {}'.format(" ".join(authors)
                                               if authors else ec602lib.AUTHWARN),file=fh)


    print('imported modules : {}'.format(" ".join(imported)),file=fh)
    print(ec602lib.code_size_report(code_metrics, {'lines': 49, 'words': 159}),file=fh)


    print('pep8 check       : {} problems.'.format(pep8_errors),file=fh)
    if pep8_errors:
        print('pep8 report',file=fh)
        print(pep8_report,file=fh)

    print('pylint score     : {}/10'.format(pylint_score),file=fh)
    print(file=fh)
    print('---- grading ----\n',file=fh)

    print('grades           :',Grade,file=fh)
    print('grade total      : {:.2f} / 6'.format(sum(Grade[x] for x in Grade)),file=fh)

    if save:
        res = fh.getvalue()
        return Grade, res
  




def main_cpp(source_file,program_to_run,original_name,faster_than_server=1,save=False):
    Grade={'specs':0,'style':0,'elegance':0,'efficiency':0}

    the_program = ec602lib.read_file(source_file)
    authors = ec602lib.get_authors(the_program, 'cpp')
    included = ec602lib.get_includes(the_program)
    

    fh = StringIO() if save else sys.stdout

    #run the specification tests

    passed_short, short_report = wordplayer_tester(program_to_run,'words680.txt',Tests_680)
    if not passed_short:
        print(short_report,file=fh)
    passed_big, big_report = wordplayer_tester(program_to_run,'words100k.txt',Tests_100k)
    if not passed_big:
        print(big_report,file=fh)
    
    if not passed_big or not passed_short:
        if save:
            return Grade,fh.getvalue()
        return


    
    code_metrics = ec602lib.code_analysis_cpp(source_file)
    
    if code_metrics['astyle']=="error":
        print('astyle is reporting a problem.',file=fh)
        code_metrics['astyle']=0

    D = code_metrics['errors']
    cpplint_count= sum(len(D[x]) for x in D)
    

    complexity = code_metrics['lines']+code_metrics['words'] + 20*code_metrics['words']/code_metrics['lines']

    rel_times= test_speed(program_to_run,faster_than_server,fh)


    eff_grade = []
    for ratio,scale in zip(rel_times,[0.5,0.2,0.1,0.05,0.05,0.05,0.05]):
        eff_grade.append(scale / ratio)


    Grade['specs']=3


    Grade['style'] = max(0,(10-cpplint_count)/20) + code_metrics['astyle']/2.0

    Grade['elegance'] = min(1.5,500/complexity) # 0.5 bonus point possible
    Grade['efficiency'] = min(2.0,sum(eff_grade)) # 1.0 bonus point possible


    print('Checking {} for EC602 submission.\n'.format(original_name),file=fh)
    print('---- analysis of your code structure ----\n',file=fh)

    print('authors          : {}'.format(" ".join(authors)
                                               if authors else ec602lib.AUTHWARN),file=fh)


    print('included libs    : {}'.format(" ".join(included)),file=fh)
    print(ec602lib.code_size_report(code_metrics, {'lines': 91, 'words': 332}),file=fh)



    print("cpplint          : {}".format("{} problems".format(cpplint_count) if cpplint_count else "ok"),file=fh)
    for e in code_metrics['errors']:
        for x in code_metrics['errors'][e][:3]:
            print('line {} ({}): {}'.format(*x),file=fh)
    print("astyle           : {:.1%} code unchanged.\n".format(code_metrics['astyle']),file=fh)

    print('---- grading ----\n',file=fh)

    print('grades           :',Grade,file=fh)
    print('grade total      : {:.2f} / 6'.format(sum(Grade[x] for x in Grade)),file=fh)

    if save:
        return Grade,fh.getvalue()

 
def pyshell(Parms,q):
      vals = main_python(**Parms)
      q.put(vals)

def cppshell(Parms,q):
      vals = main_cpp(**Parms)
      q.put(vals)


if __name__ == '__main__':
    #PD = {}
    #PD = {'source':"wordplayer.py",'program':'wordplayer.py','original':"wordplayer.py"}
    PD = {'source':"wordplayer.cpp",'program':'wordplayer','original':'wordplayer.cpp'}

    testing = 'py' if PD['source'].endswith('py') else 'cpp'

    DEBUG = True


    if not PD:
        print('please edit this file and set the value of PD to choose py or cpp to check')
        exit()

    # if C++, compile (equalizes for optimization code)
    if testing == 'cpp':
        T = run(['g++', "-std=c++14", "-O3", PD['source'], "-o", PD['program']])

        if T.returncode:
            print(T)
            quit()


    FilesNeeded = ['words100k.txt','words680.txt']

    Dir=os.listdir('.')
    for fneeded in FilesNeeded:
        if fneeded not in Dir:
            print('getting',fneeded,'from server')
            req = 'http://128.197.128.215:60217/static/content/'+fneeded
            with urllib.request.urlopen(req) as f:
               p = f.read().decode('utf-8')
               g = open(fneeded,'w')
               g.write(p)
               g.close()
    
    st = time.time()
    D = {}
    for k in range(10000):
        D[k] = random.randint(1,100)
    en = time.time()

    # server's measured time on this task is 20 ms.
    print('your 10k dictionary time',en-st)
    faster_than_server = 0.023 / (en -st)
    
    if DEBUG:
        print('your computer is {:.2%} of the speed of the server'.format(faster_than_server))

 

    if testing=='cpp':
        main_cpp(PD['source'],PD['program'],PD['original'],faster_than_server)
    else:
        main_python(PD['source'],PD['original'],faster_than_server)

    





