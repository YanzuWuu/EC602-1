// Copyright 2017 Jeff Carruthers jbc@bu.edu
//
// Solution to collision

#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>

using std::vector;
using std::cout;
using std::cerr;
using std::stod;



typedef double numbers;

const numbers NO_COLLIDE_SENTINEL = -1;
const numbers RADIUS = 5;

struct Collision {
  numbers event_time;
  int one, two;
};

struct Stone {
  std::string name;
  numbers rx, ry, vx, vy;  // position and speed
};


void collide_two_stones(Stone *one, Stone *two) {
  numbers xx = two->rx - one->rx;
  numbers xy = two->ry - one->ry;
  numbers vx = two->vx - one->vx;
  numbers vy = two->vy - one->vy;

  numbers D2 = xx * xx + xy * xy;

  numbers dot1 = vx * xx + vy * xy;

  one->vy  +=  (dot1) * (xy) / D2;
  two->vy  +=  -(dot1) * (xy) / D2;

  one->vx  += (dot1) * (xx) / D2;
  two->vx  += -(dot1) * (xx) / D2;
}


void update_position(Stone *one, const numbers dt) {
  one->rx += one->vx * dt;
  one->ry += one->vy * dt;
}


numbers collide_time(const Stone* one, const Stone* two) {
  numbers a = two->rx - one->rx;
  numbers b = two->ry - one->ry;
  numbers c = two->vx - one->vx;
  numbers d = two->vy - one->vy;
  numbers A = c * c + d * d;
  numbers B = 2 * (a * c + b * d);

  numbers C = (a * a + b * b - 4 * RADIUS * RADIUS);

  numbers rootarg = B * B - 4 * A * C;

  if (rootarg < 0) return NO_COLLIDE_SENTINEL;


  numbers root = sqrt(rootarg);

  numbers t1 = (-B - root) / (2 * A);

  if ((t1 == 0) and (a * c + b * d < 0))
    return 0;
  else if (t1 > 0)
    return t1;

  return NO_COLLIDE_SENTINEL;
}


void stone_report(const vector<Stone> & stones, numbers curr_time) {
  cout << curr_time << '\n';

  for (int i = 0; i < stones.size() ; i++) {
    cout << stones[i].name << ' '
         << stones[i].rx << ' '
         << stones[i].ry << ' '
         << stones[i].vx << ' '
         << stones[i].vy << '\n';
  }
}

Collision get_next_collision(numbers curr_time, const vector<Stone> &stones) {
  numbers next_collision = 1e38;
  numbers ct, one, two;
  Collision c;

  for (int i = 0; i < stones.size() ; i++) {
    for (int j = i + 1; j < stones.size() ; j++) {
      ct = collide_time(&stones[i], &stones[j]);
      if ((ct != NO_COLLIDE_SENTINEL) and (ct < next_collision)) {
        next_collision = ct;
        c.one = i;
        c.two = j;
      }
    }
  }

  c.event_time = next_collision + curr_time;
  return c;
}


int main(int argc, char const *argv[]) {
  cout.precision(8);

  vector<numbers> report_times;
  vector<Stone> stones;
  Stone s;
  numbers curr_time, dt;
  int one, two;  // stones involved in the event.
  try {
    for (int i = 1; i < argc; i++) {
      numbers value = std::stod(argv[i]);
      if  (value >= 0)
        report_times.push_back(value);
    }
  } catch (...) {
    return 2;
  }

  if (report_times.empty())
    return 2;

  std::sort(begin(report_times), end(report_times));

  curr_time = 0;


  std::stringstream ss;

  std::string line, rest, val;

  while (std::getline(std::cin, line)) {
    ss << line;
    try {
      ss >> s.name;
      ss >> val;
      s.rx = std::stod(val);
      ss >> val;
      s.ry = std::stod(val);
      ss >> val;
      s.vx = std::stod(val);
      ss >> val;
      s.vy = std::stod(val);
      if (ss.fail()) throw 1;
      ss >> rest;
      if (not rest.empty()) throw 1;
    } catch (...) {
      return 1;
    }

    ss.str("");
    ss.clear();

    stones.push_back(s);
  }

  int  next_report_index = 0;

  Collision collision;

  while (true) {
    // find the next collision event and the colliding object

    collision = get_next_collision(curr_time, stones);

    // print out all report times prior to collision event.

    while ( (next_report_index < report_times.size()) and
            ( (collision.event_time != NO_COLLIDE_SENTINEL) and
              (collision.event_time >= report_times[next_report_index]))
          ) {
      dt = report_times[next_report_index] - curr_time;

      for (int i = 0; i < stones.size(); i++)
        update_position(&stones[i], dt);

      curr_time = report_times[next_report_index];

      stone_report(stones, curr_time);
      next_report_index++;
    }

    // Are we done?
    if (next_report_index == report_times.size())
      break;

    // move time to collision event
    dt  = collision.event_time - curr_time;
    curr_time = collision.event_time;

    for (int i = 0; i < stones.size(); i++)
      update_position(&stones[i], dt);


    collide_two_stones(&stones[collision.one], &stones[collision.two]);
  }
  return 0;
}
