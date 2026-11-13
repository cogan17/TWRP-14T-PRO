#!/usr/bin/env python3
"""Add "Maintained by cogan17" under "OrangeFox Recovery" on the OrangeFox splash screen.

usage: ofox_splash.py <bootable/recovery/gui/theme/portrait_hdpi>

Patches the default splash (splash.xml) and the template OrangeFox rewrites it from when the
splash is customised in the settings (themes/sed/splash.xml), so the line survives that too.
Fails loudly when the upstream layout changes instead of building without the line.
"""
import sys

TEXT = 'Maintained by cogan17'


def patch_default(s):
    var = '\t\t<variable name="rec" value="%screen_h%-320"/>\n'
    end = '\t\t\t\t<text>Recovery</text>\n\t\t\t</text>\n'
    assert s.count(var) == 1 and s.count(end) == 1, 'splash.xml layout changed'
    s = s.replace(var, var + '\t\t<variable name="maint" value="%screen_h%-240"/>\n')
    return s.replace(end, end + (
        '\n\t\t\t<text>\n'
        '\t\t\t\t<placement x="540" y="%maint%" placement="4"/>\n'
        '\t\t\t\t<font resource="recovery" color="#bbbbbb"/>\n'
        f'\t\t\t\t<text>{TEXT}</text>\n'
        '\t\t\t</text>\n'))


def patch_template(s):
    # inside the #SHOWOFR# toggles: shown and hidden together with "OrangeFox Recovery"
    var = '\t\t<variable name="rec" value="%screen_h%-320"/>\n'
    rec = '\t\t\t<text>\n\t\t\t\t<placement x="540" y="%rec%" placement="4"/>\n'
    assert s.count(var) == 1 and s.count(rec) == 1, 'themes/sed/splash.xml layout changed'
    s = s.replace(var, var + '\t\t<variable name="maint" value="%screen_h%-240"/>\n')
    return s.replace(rec, (
        '\t\t\t<text>\n'
        '\t\t\t\t<placement x="540" y="%maint%" placement="4"/>\n'
        '\t\t\t\t<font resource="recovery" color="##TCOLOR#"/>\n'
        f'\t\t\t\t<text>{TEXT}</text>\n'
        '\t\t\t</text>\n') + rec)


if __name__ == '__main__':
    d = sys.argv[1]
    for name, fn in (('splash.xml', patch_default), ('themes/sed/splash.xml', patch_template)):
        p = f'{d}/{name}'
        s = open(p).read()
        if TEXT in s:
            continue  # already patched (re-run on the same tree)
        out = fn(s)
        assert out.count(TEXT) == 1
        open(p, 'w').write(out)
        print(f'{p}: {TEXT}')
