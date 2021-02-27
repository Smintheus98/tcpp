let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/repos/tcpp
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 tcpp.py
badd +1 tcpp
badd +1 term://.//5466:/usr/bin/zsh
argglobal
%argdel
$argadd tcpp.py
edit tcpp.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 23 + 23) / 47)
exe 'vert 1resize ' . ((&columns * 93 + 94) / 189)
exe '2resize ' . ((&lines * 21 + 23) / 47)
exe 'vert 2resize ' . ((&columns * 93 + 94) / 189)
exe 'vert 3resize ' . ((&columns * 95 + 94) / 189)
argglobal
setlocal fdm=syntax
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 121 - ((12 * winheight(0) + 11) / 23)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
121
normal! 09|
wincmd w
argglobal
if bufexists("term://.//5466:/usr/bin/zsh") | buffer term://.//5466:/usr/bin/zsh | else | edit term://.//5466:/usr/bin/zsh | endif
setlocal fdm=syntax
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 36 - ((20 * winheight(0) + 10) / 21)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
36
normal! 08|
wincmd w
argglobal
if bufexists("tcpp") | buffer tcpp | else | edit tcpp | endif
setlocal fdm=syntax
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 141 - ((3 * winheight(0) + 22) / 45)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
141
normal! 0
wincmd w
exe '1resize ' . ((&lines * 23 + 23) / 47)
exe 'vert 1resize ' . ((&columns * 93 + 94) / 189)
exe '2resize ' . ((&lines * 21 + 23) / 47)
exe 'vert 2resize ' . ((&columns * 93 + 94) / 189)
exe 'vert 3resize ' . ((&columns * 95 + 94) / 189)
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
