import re

# s/ \[#[0-9a-z]\+\]$//g
# s/^\*\*\*/###/g
# s/^\*\*/##/g
# s/^\*/#/g
# s/^---/        -/g
# s/^--/    -/g
# s/^\(\s*\)-\([^ ]\)/\1- \2/g
# s/&br/<br>/g
# s/^#pre{*/```/g
# s/^}}*/```/g
# s/%%/~~/g'
# "s/^\#lsx/`echo -ne '\u0024'`lsx()"


def _sub(pattern, repl, string, count=0, flags=0):
    s = re.sub(pattern, repl, string, count=count, flags=re.MULTILINE | flags)
    return s


def delete_hash(src):
    s = _sub(r" \[#[0-9a-z]+\]$", "", src)
    return s


def convert_headings(src):
    s1 = _sub(r"^\*\*\*", "###", src)
    s2 = _sub(r"^\*\*", "##", s1)
    s3 = _sub(r"^\*", "#", s2)

    return s3


def convert_bullets(src):
    s1 = _sub(r"^---", "        -", src)
    s2 = _sub(r"^--", "    -", s1)
    s3 = _sub(r"^(\s*)-([^ ])", r"\1- \2", s2)

    return s3


def convert_br(src):
    s = _sub(r"&br", "<br>", src)
    return s


def convert_pre(src):
    s1 = _sub(r"^#pre{*", "```", src)
    s2 = _sub(r"^}}*", "```", s1)

    return s2


def convert_strike(src):
    s = _sub(r"%%", "~~", src)

    return s


def convert_lsx(src):
    s = _sub(r"^\#lsx", r"$lsx()", src)

    return s


def convert(src):
    funcs = [
        delete_hash,
        convert_headings,
        convert_bullets,
        convert_br,
        convert_pre,
        convert_strike,
        convert_lsx,
    ]

    s = src
    for f in funcs:
        s = f(s)

    return s


def _run_test():
    text = r"""hoge [#fuga]
    *** hoge
    ** fuga
    * piyo
    -hoge
    --fuga
    ---piyo
    &br
    #pre{
        hoge
    }
    #pre{{
    fuga
    hogefuga
    }}
    %%hegu%%
    #lsx
    """

    out = convert(text)
    print(out)


if __name__ == "__main__":
    _run_test()
