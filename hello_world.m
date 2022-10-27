clc; clear; close all;

x = input("");
strings = repelem("Hello world!", x);
disp(join(strings, newline));
