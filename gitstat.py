#!/usr/bin/env python3

import matplotlib.pyplot as plt
from github import Github
from getpass import getpass

github_user = "your_user"

data = {2015: {"JonathanSalwan": ["Triton"],
               "k0retux": ["fuddly"],
               "eurecom-s3": ["avatar-python"],
               "stemjail": ["stemjail"]},
        2014: {"AndroidHooker": ["hooker"],
               # "quarkslab": ["irma-frontend", "irma-brain", "irma-probe", "irma-common"],
               "frederic": ["dfb-wireshark-dissector", "pflupg-tool"]},
        2013: {"ANSSI-FR": ["parsifal"]},
        2012: {"netzob" :["netzob"]},
        2011: {"sduverger": ["ramooflax"]},
        2008: {"thorkill": ["eresi"]},
    }


if __name__ == "__main__":
    git = Github(your_user, getpass())
    total = dict()
    for year, thingz in data.items():
        for dude, projects in thingz.items():
            for project in projects:
                ma_daug = git.get_user(dude).get_repo(project).get_stats_commit_activity()
                total["%s/%s" %(dude, project)] = ([i.week for i in ma_daug], [i.total for i in ma_daug])

    fig = plt.figure()
    rect = fig.patch.set_alpha(0.5)
    ax = fig.add_subplot(111)
    fmts = ["g-", "r-", "b-", "y-", "c-", "m-", "k-"]
    for label, a in total.items():
        ax.plot_date(a[0], a[1], fmt=fmts.pop(), label=label, linewidth=1.5)
        if not fmts:
            fmts = ["g-", "r-", "b-", "c-", "m-", "k-"]
    ax.set_xlabel("Date")
    ax.set_ylabel("Commit nb")
    plt.legend(loc="upper left")
    plt.show()
