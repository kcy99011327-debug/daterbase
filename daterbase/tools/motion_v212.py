#!/usr/bin/env python3
"""Daterbase 화면 움직임 2차 (v2.1.2) 패치.

사용법:  python3 tools/motion_v212.py index.html
- 이미 적용된 파일이면 아무것도 하지 않고 끝나요.
- 찾는 코드가 없으면(앱 코드가 바뀌었으면) 멈추고 어느 항목인지 알려 줘요.

바뀌는 것
 1. 대시보드(보드) 블록 등장 효과 없앰
 2. 사이드바 메인탭 아이콘: 마우스 올릴 때 옆으로 움직이는 효과 없앰
 3. 스레드 카드: 마우스 올릴 때 들리는 효과 없앰
 4. 앱 아이콘: 누를 때 꾹 눌렸다 통 튀어나오는 클릭 효과
 5. 다이어리 폰: 나타날 때 떠오름, 기울기 변화 부드럽게, 잠금화면이 위로 스르르 열리고 닫힘, 카드 차례로 등장
 6. 타임테이블: 일정 블록 옮기기·늘리기가 15분 칸에 딱딱 맞음 (마우스·터치)
 7. 커미션 포스터: 벽에 테이프로 붙인 포스터 느낌 (살짝 기울기, 테이프, 붙는 애니메이션, 간격 넓힘)
 8. 레코드 갤러리: 그림이 차례로 떠오르고, 마우스 올리면 살짝 확대 / 크게 보기 열 때 부드럽게
 9. 레코드 책: 책이 차례로 등장, 마우스 올리면 표지가 살짝 펼쳐지는 느낌, 읽기 화면 부드럽게 열림
"""
import sys

MARK = '/* ═══ 화면 움직임 2차 (v2.1.2) ═══ */'

CSS = MARK + r'''
/* 1·2·3 없애기 */
.mboard__canvas>.mbi{animation:none!important}
.sidebar .brand:not(.is-active):hover{translate:none!important}
.bltile:hover{translate:none!important;box-shadow:none!important}

/* 4 앱 아이콘 클릭 */
.apic__ic{transition:transform .42s cubic-bezier(.34,1.56,.64,1),box-shadow .2s,filter .2s}
.apic:active .apic__ic{transform:scale(.84)!important;filter:brightness(.92);transition-duration:.09s}
.apic:focus-visible .apic__ic{outline:2px solid var(--accent-strong);outline-offset:3px}

/* 5 다이어리 폰 */
@keyframes dbmPhoneIn{from{opacity:0;translate:0 28px}to{opacity:1;translate:0 0}}
.dyph{animation:dbmPhoneIn .7s var(--dbm-e) backwards}
.dyph__frame{transition:transform .55s var(--dbm-e),box-shadow .4s}
.dyph__frame.is-drag{transition:none!important}
.dyph__lock{display:flex!important;transform:translateY(-104%);opacity:0;pointer-events:none;transition:transform .55s cubic-bezier(.65,0,.35,1),opacity .35s .12s}
.dyph.is-lock .dyph__lock,.mboard.is-capturing .dyph__lock{transform:none;opacity:1;pointer-events:auto;transition:transform .5s var(--dbm-e),opacity .2s}
.mboard.is-capturing .dyph__lock{transition:none!important}
.dyph__grid>*{animation:dbmRise .5s var(--dbm-e) backwards;animation-delay:calc(var(--dbm-i,0)*50ms + 150ms)}
.dyph__grid .dyin__card{transition:transform .25s var(--dbm-e),box-shadow .25s}
.dyph__grid .dyin__card:hover{transform:translateY(-2px);box-shadow:0 8px 16px -10px #0006}
.dyph__scr{scroll-behavior:smooth}

/* 7 커미션 포스터: 벽에 붙인 포스터 */
@keyframes dbmStick{0%{opacity:0;scale:1.14;translate:0 -22px}55%{opacity:1}100%{opacity:1;scale:1;translate:0 0}}
.cm-gal.cm-mas{margin-top:14px}
.cm-mas>.cm-tile.cm-post{overflow:visible;rotate:calc((var(--h1) - 180) * .012deg);box-shadow:0 1px 2px #0002,0 14px 24px -14px #0008;transition:rotate .45s var(--dbm-e),scale .45s var(--dbm-e),box-shadow .35s;animation:dbmStick .65s cubic-bezier(.3,1.35,.5,1) backwards;animation-delay:calc(var(--dbm-i,0)*80ms)}
.cm-mas>.cm-tile.cm-post:hover{rotate:0deg;scale:1.025;z-index:3;box-shadow:0 2px 3px #0002,0 26px 40px -20px #0009}
.cm-mas>.cm-post .cm-cap,.cm-mas>.cm-post .cm-pic{border-radius:0}
.cm-mas>.cm-post::before,.cm-mas>.cm-post::after{content:"";position:absolute;z-index:4;pointer-events:none;width:78px;height:22px;background:color-mix(in srgb,#efe3c4 82%,transparent);box-shadow:0 1px 2px #0002;clip-path:polygon(3% 0,97% 4%,100% 30%,96% 52%,100% 78%,97% 100%,2% 96%,0 70%,4% 48%,0 22%)}
.cm-mas>.cm-post::before{top:-10px;left:50%;margin-left:-39px;rotate:calc((var(--h2) - 180) * .02deg)}
.cm-mas>.cm-post::after{display:none}
.cm-mas>.cm-post:nth-child(3n+2)::before{left:-14px;top:6px;margin:0;width:62px;rotate:-42deg}
.cm-mas>.cm-post:nth-child(3n+2)::after{display:block;right:-14px;left:auto;top:6px;width:62px;rotate:42deg}
.cm-mas>.cm-post .cm-ptag{rotate:-3deg}
.cm-mas>:nth-child(1){--dbm-i:0}.cm-mas>:nth-child(2){--dbm-i:1}.cm-mas>:nth-child(3){--dbm-i:2}.cm-mas>:nth-child(4){--dbm-i:3}.cm-mas>:nth-child(5){--dbm-i:4}.cm-mas>:nth-child(6){--dbm-i:5}.cm-mas>:nth-child(7){--dbm-i:6}.cm-mas>:nth-child(8){--dbm-i:7}.cm-mas>:nth-child(n+9){--dbm-i:8}

/* 8 레코드 갤러리 */
.gal-mas>.gal-tile{animation:dbmRise .55s var(--dbm-e) backwards;animation-delay:calc(var(--dbm-i,0)*45ms)}
.gal-mas>.gal-tile .cm-pic{transition:scale .5s var(--dbm-e),filter .3s}
.gal-mas>.gal-tile:hover .cm-pic{scale:1.045}
.gal-lb{animation:dbmFade .25s ease backwards}
.gal-lb__pic{animation:dbmModal .45s var(--dbm-e) backwards}

/* 9 레코드 책 */
.blog__grid>.blog__bk{animation:dbmRise .55s var(--dbm-e) backwards;animation-delay:calc(var(--dbm-i,0)*55ms)}
.blog__bk .blog__cov{transform-origin:0 50%;transition:transform .5s var(--dbm-e),box-shadow .5s var(--dbm-e)}
.blog__bk .blog__cov::after{content:"";position:absolute;left:0;top:0;bottom:0;width:7%;background:linear-gradient(90deg,#0003,#fff2 60%,transparent);pointer-events:none}
.blog__bk:hover .blog__cov{outline:none!important;transform:perspective(800px) rotateY(-16deg) translateX(3px);box-shadow:14px 16px 26px -14px #0009}
.blog__bk:active .blog__cov{transform:perspective(800px) rotateY(-24deg) translateX(5px)}
.eb__spread{animation:dbmModal .5s var(--dbm-e) backwards}

:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(1){--dbm-i:0}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(2){--dbm-i:1}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(3){--dbm-i:2}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(4){--dbm-i:3}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(5){--dbm-i:4}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(6){--dbm-i:5}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(7){--dbm-i:6}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(8){--dbm-i:7}:is(.gal-mas,.blog__grid,.dyph__grid)>:nth-child(n+9){--dbm-i:8}

@media (prefers-reduced-motion:reduce){.dyph,.dyph__lock,.dyph__grid>*,.cm-mas>.cm-post,.gal-mas>.gal-tile,.blog__grid>.blog__bk,.eb__spread,.gal-lb,.gal-lb__pic{animation-duration:.01ms!important;animation-delay:0s!important;transition-duration:.01ms!important}}
'''

# (설명, 찾을 코드, 바꿀 코드)
JS = [
    ('타임테이블 마우스로 옮기기·늘리기 15분 스냅',
     'd=Math.round(dy/HH*60/5)*5;',
     'd=(()=>{let r0=dy/HH*60,bs=mode==="move"?e.a:(e.b%1440===1439?e.b+1:e.b);return Math.round((bs+r0)/15)*15-bs})();'),
    ('타임테이블 터치로 옮기기·늘리기 15분 스냅',
     'd=Math.round((t.clientY-y0)/HH*60/5)*5;',
     'd=(()=>{let r0=(t.clientY-y0)/HH*60,bs=sz?(e.b%1440===1439?e.b+1:e.b):e.a;return Math.round((bs+r0)/15)*15-bs})();'),
    ('커미션 포스터 사이 간격 넓히기',
     'let gp=14,n=W<560?2:Math.max(2,Math.min(5,Math.round(W/320)))',
     'let gp=26,n=W<560?2:Math.max(2,Math.min(5,Math.round(W/320)))'),
]


def apply(t):
    if MARK in t:
        return t, False
    for name, a, b in JS:
        n = t.count(a)
        if n != 1:
            raise SystemExit(f'멈춤: "{name}" 자리를 찾지 못했어요 (찾은 개수 {n})')
        t = t.replace(a, b)
    if '화면 움직임 (기본)' not in t:
        raise SystemExit('멈춤: 1차 화면 움직임(v2.1.1) CSS가 없어요. 먼저 적용해야 해요.')
    t = t.rstrip() + '\n<style id="dbm-css2">' + CSS + '</style>\n'
    return t, True


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
    src = open(path, encoding='utf-8').read()
    out, changed = apply(src)
    if changed:
        open(path, 'w', encoding='utf-8').write(out)
        print('적용했어요:', path)
    else:
        print('이미 적용돼 있어요:', path)
