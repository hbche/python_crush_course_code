from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""

    try:
        # contents = Path(path).read_text(encoding="utf-8")
        contents = Path(path).read_text()
    except FileNotFoundError:
        # 静默失败，什么都不做
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


def word_count(path, word):
    """统计word在path对应文件中出现多少次"""

    contents = path.read_text(encoding="utf-8")
    count = contents.count(word)
    print(f"The {word} has {count} in the {path} file.")
    # word_count = 0
    # for content_word in contents.split():
    #     if content_word == word:
    #         word_count += 1
    # print(f"The {word} has {word_count} in the {path} file.")


word_count(Path('alice.txt'), 'the ')