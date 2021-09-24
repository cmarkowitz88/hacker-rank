#!/bin/python3

def most_freq_char(inStr):

    tmp = inStr
    chr_dict = {}

    for ch in tmp:
        if ch in chr_dict:
            chr_dict[ch] += 1
        else:
            chr_dict[ch] = 1

    print(max(chr_dict, key=chr_dict.get))

ans = most_freq_char('abcdefhlkjladjfaldjfaldjfalsdjfwpeour02378402348023480234pweiurpweirpweirpweirpweipj')