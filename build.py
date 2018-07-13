from jinja2 import Template
import subprocess

with open('pyconkr-2018.html') as file:
    template = Template(file.read())

sponsor_levels = [
    {
        'name': '다이아몬드',
        'sponsors': [
            {
                'name': '뱅크샐러드',
            },
            {
                'name': '하이퍼커넥트',
            },
        ],
    },
    {
        'name': '사파이어',
        'sponsors': [
            {
                'name': '루닛',
            },
        ],
    },
    {
        'name': '플래티넘',
        'sponsors': [
            {
                'name': '알지피코리아',
            },
            {
                'name': '패스트캠퍼스',
            },
            {
                'name': '구글',
            },
        ],
    },
    {
        'name': '골드',
        'sponsors': [
            {
                'name': 'ICON',
            },
            {
                'name': '리디 주식회사',
            },
            {
                'name': '센드버드',
            },
            {
                'name': '라인',
            },
            {
                'name': '스포카',
            },
            {
                'name': '코인원',
            },
            {
                'name': 'JetBrains',
            },
            {
                'name': '래블업',
            },
        ],
    },
    {
        'name': '실버',
        'sponsors': [
            {
                'name': '피플펀드',
            },
            {
                'name': '번개장터',
            },
            {
                'name': 'HBSmith',
            },
            {
                'name': 'MyMusicTaste',
            },
            {
                'name': '스타트링크',
            },
        ],
    },
]
page = template.render({
    'sponsor_levels': sponsor_levels,
})

p = subprocess.Popen(["prince", "-", "-o", "out.pdf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
outs, errs = p.communicate(page.encode("utf-8"))
