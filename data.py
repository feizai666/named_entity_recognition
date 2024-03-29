from os.path import join
from codecs import open


# def build_corpus(split, make_vocab=True, data_dir="./ResumeNER"):
#     """读取数据"""
#     assert split in ['train', 'dev', 'test']

#     word_lists = []
#     tag_lists = []
#     with open(join(data_dir, split+".char.bmes"), 'r', encoding='utf-8') as f:
#         word_list = []
#         tag_list = []
#         for line in f:
#             if line != '\n':
#                 word, tag = line.strip('\n').split()
#                 word_list.append(word)
#                 tag_list.append(tag)
#             else:
#                 word_lists.append(word_list)
#                 tag_lists.append(tag_list)
#                 word_list = []
#                 tag_list = []

#     # 如果make_vocab为True，还需要返回word2id和tag2id
#     if make_vocab:
#         word2id = build_map(word_lists)
#         tag2id = build_map(tag_lists)
#         return word_lists, tag_lists, word2id, tag2id
#     else:
#         return word_lists, tag_lists
def build_corpus(split, make_vocab=True, data_dir="./ResumeNER"):
    """读取数据"""
    assert split in ['train', 'dev', 'test']

    word_lists = []
    tag_lists = []
    with open(join(data_dir, split+".char.bmes"), 'r', encoding='utf-8') as f:
        word_list = []
        tag_list = []
        for line in f:
            if line.strip() != '':  # 添加检查，确保line不仅仅是换行符
                parts = line.strip('\n').split()
                if len(parts) == 2:  # 确保行有两部分，单词和标签
                    word, tag = parts
                    word_list.append(word)
                    tag_list.append(tag)
                else:
                    print(f"格式错误的行: {line.strip()}")  # 可选：打印格式错误的行
            else:
                if word_list and tag_list:  # 确保word_list和tag_list不为空
                    word_lists.append(word_list)
                    tag_lists.append(tag_list)
                word_list = []
                tag_list = []

    # 如果make_vocab为True，还需要返回word2id和tag2id
    if make_vocab:
        word2id = build_map(word_lists)
        tag2id = build_map(tag_lists)
        return word_lists, tag_lists, word2id, tag2id
    else:
        return word_lists, tag_lists

def build_map(lists):
    maps = {}
    for list_ in lists:
        for e in list_:
            if e not in maps:
                maps[e] = len(maps)

    return maps
