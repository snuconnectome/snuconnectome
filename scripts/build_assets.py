"""Build original schematic artwork for the GitHub profile; no network calls."""
from pathlib import Path
import math
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get('PROFILE_FONT_DIR',
    str(Path.home() / '.fonts/pretendard/public/static/alternative')))
OUT = ROOT / 'assets'
THEMES = {
    'light': dict(bg='#F5F8FC', ink='#102A43', muted='#465E71',
                  line='#DCE8EF', teal='#087F8C', purple='#6655A5', blue='#376CBA'),
    'dark': dict(bg='#102A43', ink='#F5F8FC', muted='#B8CEDD',
                 line='#2B4B63', teal='#6BD4D5', purple='#B7A6E8', blue='#87B8F7'),
}


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_DIR / f'Pretendard-{"Bold" if bold else "Regular"}.ttf'), size)


def text(d, xy, value, size, fill, bold=False):
    d.text(xy, value, font=font(size, bold), fill=fill, anchor='lt')


def wave(d, box, color, phase=0, freq=2, width=3):
    x, y, w, h = box
    points = [(x+i*w/240, y+h*.5+math.sin(i/240*math.tau*freq+phase)*h*.36
               + math.sin(i/240*math.tau*freq*2.3)*h*.1) for i in range(241)]
    d.line(points, fill=color, width=width)


def network(d, box, p):
    """Stylized bilateral connectome, deliberately not anatomical data."""
    x,y,w,h=box
    nodes=[]
    for side in (-1,1):
        for i in range(36):
            a=i*2.39996
            r=math.sqrt((i+.5)/36)
            px=x+w*.5+side*w*.22+math.cos(a)*r*w*.21
            py=y+h*.47+math.sin(a)*r*h*.42
            nodes.append((px,py))
    for i,a in enumerate(nodes):
        near=sorted(enumerate(nodes),key=lambda v: math.dist(a,v[1]))[1:4]
        for j,b in near:
            if j>i: d.line([a,b],fill=p['line'],width=2)
        if i%7==0:
            b=nodes[(i+36)%72]
            d.line([a,b],fill=p['teal'],width=2)
    for i,(px,py) in enumerate(nodes):
        r=6 if i%7==0 else 3
        c=p['teal'] if i%3 else p['purple']
        d.ellipse((px-r,py-r,px+r,py+r),fill=c)
    for k in range(3):
        wave(d,(x+w*.1,y+h*.93+k*13,w*.8,23),p['teal'] if k==1 else p['line'],k,2,2)


def save(im, name):
    OUT.mkdir(exist_ok=True)
    im.save(OUT / f'{name}.png', optimize=True)


def hero(theme, mobile=False):
    p=THEMES[theme]
    w,h=(800,790) if mobile else (1600,660)
    im=Image.new('RGB',(w,h),p['bg']); d=ImageDraw.Draw(im)
    if mobile:
        network(d,(420,410,340,300),p)
        text(d,(52,50),'Jiook Cha',100,p['ink'],True)
        text(d,(54,170),'차지욱  /  Connectome Lab',37,p['muted'])
        text(d,(52,268),'Understanding',64,p['ink'],True)
        text(d,(52,345),'human differences.',64,p['ink'],True)
        text(d,(54,470),'Brain.',40,p['teal'],True)
        text(d,(54,526),'Mind.',40,p['teal'],True)
        text(d,(54,582),'Intelligence.',40,p['teal'],True)
        text(d,(54,718),'Seoul National University',30,p['muted'])
    else:
        network(d,(1020,70,525,480),p)
        text(d,(74,66),'Jiook Cha',118,p['ink'],True)
        text(d,(78,211),'차지욱  /  Connectome Lab',37,p['muted'])
        text(d,(74,316),'Understanding',76,p['ink'],True)
        text(d,(74,406),'human differences.',76,p['ink'],True)
        text(d,(78,565),'Brain, mind & intelligence',32,p['teal'],True)
        text(d,(1070,578),'Seoul National University',26,p['muted'])
    save(im,f'hero-{theme}'+('-mobile' if mobile else ''))


def card(theme, name):
    p=THEMES[theme]; im=Image.new('RGB',(800,470),p['bg']); d=ImageDraw.Draw(im)
    color={'SwiFT':p['blue'],'SwiFUN':p['teal'],'MBBN':p['purple'],'NeuroMamba':p['teal']}[name]
    if name=='SwiFT':
        for layer in range(4):
            ox=100+layer*125; oy=76+layer*12
            for row in range(4):
                for col in range(4):
                    x=ox+col*32-row*11; y=oy+row*31
                    fill=color if (col+row+layer)%5==0 else p['line']
                    d.rounded_rectangle((x,y,x+25,y+25),radius=3,fill=fill)
    elif name=='SwiFUN':
        for i in range(3): wave(d,(48,66+i*57,280,44),color,i*.8,2+i*.3,4)
        d.line((360,151,430,151),fill=p['muted'],width=3)
        d.polygon([(430,151),(419,144),(419,158)],fill=p['muted'])
        for row in range(5):
            for col in range(7):
                c=color if (row*7+col)%4 in (0,1) else p['line']
                x=480+col*35;y=67+row*36
                d.rounded_rectangle((x,y,x+26,y+26),radius=5,fill=c)
    elif name=='MBBN':
        for i,c in enumerate([p['blue'],p['purple'],p['teal']]):
            wave(d,(48,53+i*70,700,59),c,i*.6,1.5+i*2.8,4)
    else:
        for i in range(6):
            x=65+i*122
            if i<5: d.line((x+45,149,x+122,149),fill=p['muted'],width=3)
            d.rounded_rectangle((x,115,x+54,182),radius=12,fill=p['line'])
            d.ellipse((x+18,140,x+36,158),fill=color)
        wave(d,(55,64,680,32),p['blue'],0,3,3)
        wave(d,(55,213,680,32),color,1,2,3)
    text(d,(46,309),name,84 if name!='NeuroMamba' else 78,p['ink'],True)
    captions={'SwiFT':'4D fMRI transformer','SwiFUN':'Rest to task prediction',
              'MBBN':'Multi-band brain network','NeuroMamba':'State-space fMRI model'}
    text(d,(50,410),captions[name],29,p['muted'])
    save(im,f'card-{name.lower()}-{theme}')


def main():
    for theme in THEMES:
        hero(theme)
        hero(theme,True)
        for name in ['SwiFT','SwiFUN','MBBN','NeuroMamba']: card(theme,name)
    print(f'Built 12 assets in {OUT}')


if __name__=='__main__': main()
