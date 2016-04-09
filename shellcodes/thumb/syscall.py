syscall_table = {}
syscall_table[285]="accept"
syscall_table[33]="access"
syscall_table[51]="acct"
syscall_table[309]="add_key"
syscall_table[124]="adjtimex"
syscall_table[27]="alarm"
syscall_table[270]="arm_fadvise64_64"
syscall_table[341]="arm_sync_file_range"
syscall_table[134]="bdflush"
syscall_table[282]="bind"
syscall_table[45]="brk"
syscall_table[184]="capget"
syscall_table[185]="capset"
syscall_table[12]="chdir"
syscall_table[15]="chmod"
syscall_table[182]="chown"
syscall_table[212]="chown32"
syscall_table[61]="chroot"
syscall_table[264]="clock_getres"
syscall_table[263]="clock_gettime"
syscall_table[265]="clock_nanosleep"
syscall_table[262]="clock_settime"
syscall_table[120]="clone"
syscall_table[6]="close"
syscall_table[283]="connect"
syscall_table[8]="creat"
syscall_table[129]="delete_module"
syscall_table[41]="dup"
syscall_table[63]="dup2"
syscall_table[250]="epoll_create"
syscall_table[251]="epoll_ctl"
syscall_table[252]="epoll_wait"
syscall_table[351]="eventfd"
syscall_table[11]="execve"
syscall_table[1]="exit"
syscall_table[248]="exit_group"
syscall_table[334]="faccessat"
syscall_table[352]="fallocate"
syscall_table[133]="fchdir"
syscall_table[94]="fchmod"
syscall_table[333]="fchmodat"
syscall_table[95]="fchown"
syscall_table[207]="fchown32"
syscall_table[325]="fchownat"
syscall_table[55]="fcntl"
syscall_table[221]="fcntl64"
syscall_table[148]="fdatasync"
syscall_table[231]="fgetxattr"
syscall_table[234]="flistxattr"
syscall_table[143]="flock"
syscall_table[2]="fork"
syscall_table[237]="fremovexattr"
syscall_table[228]="fsetxattr"
syscall_table[108]="fstat"
syscall_table[197]="fstat64"
syscall_table[327]="fstatat64"
syscall_table[100]="fstatfs"
syscall_table[267]="fstatfs64"
syscall_table[118]="fsync"
syscall_table[93]="ftruncate"
syscall_table[194]="ftruncate64"
syscall_table[240]="futex"
syscall_table[326]="futimesat"
syscall_table[345]="getcpu"
syscall_table[183]="getcwd"
syscall_table[141]="getdents"
syscall_table[217]="getdents64"
syscall_table[50]="getegid"
syscall_table[202]="getegid32"
syscall_table[49]="geteuid"
syscall_table[201]="geteuid32"
syscall_table[47]="getgid"
syscall_table[200]="getgid32"
syscall_table[80]="getgroups"
syscall_table[205]="getgroups32"
syscall_table[105]="getitimer"
syscall_table[320]="get_mempolicy"
syscall_table[287]="getpeername"
syscall_table[132]="getpgid"
syscall_table[65]="getpgrp"
syscall_table[20]="getpid"
syscall_table[64]="getppid"
syscall_table[96]="getpriority"
syscall_table[171]="getresgid"
syscall_table[211]="getresgid32"
syscall_table[165]="getresuid"
syscall_table[209]="getresuid32"
syscall_table[76]="getrlimit"
syscall_table[339]="get_robust_list"
syscall_table[77]="getrusage"
syscall_table[147]="getsid"
syscall_table[286]="getsockname"
syscall_table[295]="getsockopt"
syscall_table[224]="gettid"
syscall_table[78]="gettimeofday"
syscall_table[24]="getuid"
syscall_table[199]="getuid32"
syscall_table[229]="getxattr"
syscall_table[128]="init_module"
syscall_table[317]="inotify_add_watch"
syscall_table[316]="inotify_init"
syscall_table[318]="inotify_rm_watch"
syscall_table[247]="io_cancel"
syscall_table[54]="ioctl"
syscall_table[244]="io_destroy"
syscall_table[245]="io_getevents"
syscall_table[315]="ioprio_get"
syscall_table[314]="ioprio_set"
syscall_table[243]="io_setup"
syscall_table[246]="io_submit"
syscall_table[117]="ipc"
syscall_table[347]="kexec_load"
syscall_table[311]="keyctl"
syscall_table[37]="kill"
syscall_table[16]="lchown"
syscall_table[198]="lchown32"
syscall_table[230]="lgetxattr"
syscall_table[9]="link"
syscall_table[330]="linkat"
syscall_table[284]="listen"
syscall_table[232]="listxattr"
syscall_table[233]="llistxattr"
syscall_table[140]="_llseek"
syscall_table[249]="lookup_dcookie"
syscall_table[236]="lremovexattr"
syscall_table[19]="lseek"
syscall_table[227]="lsetxattr"
syscall_table[107]="lstat"
syscall_table[196]="lstat64"
syscall_table[220]="madvise"
syscall_table[319]="mbind"
syscall_table[219]="mincore"
syscall_table[39]="mkdir"
syscall_table[323]="mkdirat"
syscall_table[14]="mknod"
syscall_table[324]="mknodat"
syscall_table[150]="mlock"
syscall_table[152]="mlockall"
syscall_table[90]="mmap"
syscall_table[192]="mmap2"
syscall_table[21]="mount"
syscall_table[344]="move_pages"
syscall_table[125]="mprotect"
syscall_table[279]="mq_getsetattr"
syscall_table[278]="mq_notify"
syscall_table[274]="mq_open"
syscall_table[277]="mq_timedreceive"
syscall_table[276]="mq_timedsend"
syscall_table[275]="mq_unlink"
syscall_table[163]="mremap"
syscall_table[304]="msgctl"
syscall_table[303]="msgget"
syscall_table[302]="msgrcv"
syscall_table[301]="msgsnd"
syscall_table[144]="msync"
syscall_table[151]="munlock"
syscall_table[153]="munlockall"
syscall_table[91]="munmap"
syscall_table[162]="nanosleep"
syscall_table[142]="_newselect"
syscall_table[169]="nfsservctl"
syscall_table[34]="nice"
syscall_table[5]="open"
syscall_table[322]="openat"
syscall_table[29]="pause"
syscall_table[271]="pciconfig_iobase"
syscall_table[272]="pciconfig_read"
syscall_table[273]="pciconfig_write"
syscall_table[136]="personality"
syscall_table[42]="pipe"
syscall_table[218]="pivot_root"
syscall_table[168]="poll"
syscall_table[172]="prctl"
syscall_table[180]="pread64"
syscall_table[26]="ptrace"
syscall_table[181]="pwrite64"
syscall_table[131]="quotactl"
syscall_table[3]="read"
syscall_table[225]="readahead"
syscall_table[89]="readdir"
syscall_table[85]="readlink"
syscall_table[332]="readlinkat"
syscall_table[145]="readv"
syscall_table[88]="reboot"
syscall_table[291]="recv"
syscall_table[292]="recvfrom"
syscall_table[297]="recvmsg"
syscall_table[253]="remap_file_pages"
syscall_table[235]="removexattr"
syscall_table[38]="rename"
syscall_table[329]="renameat"
syscall_table[310]="request_key"
syscall_table[0]="restart_syscall"
syscall_table[40]="rmdir"
syscall_table[174]="rt_sigaction"
syscall_table[176]="rt_sigpending"
syscall_table[175]="rt_sigprocmask"
syscall_table[178]="rt_sigqueueinfo"
syscall_table[173]="rt_sigreturn"
syscall_table[179]="rt_sigsuspend"
syscall_table[177]="rt_sigtimedwait"
syscall_table[242]="sched_getaffinity"
syscall_table[155]="sched_getparam"
syscall_table[159]="sched_get_priority_max"
syscall_table[160]="sched_get_priority_min"
syscall_table[157]="sched_getscheduler"
syscall_table[161]="sched_rr_get_interval"
syscall_table[241]="sched_setaffinity"
syscall_table[154]="sched_setparam"
syscall_table[156]="sched_setscheduler"
syscall_table[158]="sched_yield"
syscall_table[82]="select"
syscall_table[300]="semctl"
syscall_table[299]="semget"
syscall_table[298]="semop"
syscall_table[312]="semtimedop"
syscall_table[289]="send"
syscall_table[187]="sendfile"
syscall_table[239]="sendfile64"
syscall_table[296]="sendmsg"
syscall_table[290]="sendto"
syscall_table[121]="setdomainname"
syscall_table[139]="setfsgid"
syscall_table[216]="setfsgid32"
syscall_table[138]="setfsuid"
syscall_table[215]="setfsuid32"
syscall_table[46]="setgid"
syscall_table[214]="setgid32"
syscall_table[81]="setgroups"
syscall_table[206]="setgroups32"
syscall_table[74]="sethostname"
syscall_table[104]="setitimer"
syscall_table[321]="set_mempolicy"
syscall_table[57]="setpgid"
syscall_table[97]="setpriority"
syscall_table[71]="setregid"
syscall_table[204]="setregid32"
syscall_table[170]="setresgid"
syscall_table[210]="setresgid32"
syscall_table[164]="setresuid"
syscall_table[208]="setresuid32"
syscall_table[70]="setreuid"
syscall_table[203]="setreuid32"
syscall_table[75]="setrlimit"
syscall_table[338]="set_robust_list"
syscall_table[66]="setsid"
syscall_table[294]="setsockopt"
syscall_table[256]="set_tid_address"
syscall_table[79]="settimeofday"
syscall_table[23]="setuid"
syscall_table[213]="setuid32"
syscall_table[226]="setxattr"
syscall_table[305]="shmat"
syscall_table[308]="shmctl"
syscall_table[306]="shmdt"
syscall_table[307]="shmget"
syscall_table[293]="shutdown"
syscall_table[67]="sigaction"
syscall_table[186]="sigaltstack"
syscall_table[349]="signalfd"
syscall_table[73]="sigpending"
syscall_table[126]="sigprocmask"
syscall_table[119]="sigreturn"
syscall_table[72]="sigsuspend"
syscall_table[281]="socket"
syscall_table[102]="socketcall"
syscall_table[288]="socketpair"
syscall_table[340]="splice"
syscall_table[106]="stat"
syscall_table[195]="stat64"
syscall_table[99]="statfs"
syscall_table[266]="statfs64"
syscall_table[25]="stime"
syscall_table[115]="swapoff"
syscall_table[87]="swapon"
syscall_table[83]="symlink"
syscall_table[331]="symlinkat"
syscall_table[36]="sync"
syscall_table[113]="syscall"
syscall_table[0]="SYSCALL_BASE"
syscall_table[149]="_sysctl"
syscall_table[135]="sysfs"
syscall_table[116]="sysinfo"
syscall_table[103]="syslog"
syscall_table[342]="tee"
syscall_table[268]="tgkill"
syscall_table[13]="time"
syscall_table[257]="timer_create"
syscall_table[261]="timer_delete"
syscall_table[350]="timerfd"
syscall_table[354]="timerfd_gettime"
syscall_table[353]="timerfd_settime"
syscall_table[260]="timer_getoverrun"
syscall_table[259]="timer_gettime"
syscall_table[258]="timer_settime"
syscall_table[43]="times"
syscall_table[238]="tkill"
syscall_table[92]="truncate"
syscall_table[193]="truncate64"
syscall_table[191]="ugetrlimit"
syscall_table[60]="umask"
syscall_table[22]="umount"
syscall_table[52]="umount2"
syscall_table[122]="uname"
syscall_table[10]="unlink"
syscall_table[328]="unlinkat"
syscall_table[337]="unshare"
syscall_table[86]="uselib"
syscall_table[62]="ustat"
syscall_table[30]="utime"
syscall_table[348]="utimensat"
syscall_table[269]="utimes"
syscall_table[190]="vfork"
syscall_table[111]="vhangup"
syscall_table[343]="vmsplice"
syscall_table[313]="vserver"
syscall_table[114]="wait4"
syscall_table[280]="waitid"
syscall_table[4]="write"
syscall_table[146]="writev"

def get(no):
    return syscall_table[no]