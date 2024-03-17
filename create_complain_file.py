from get_paraphrase import *
import json

def test_file(group):
    answer = []
    print(len(group))
    for ele in group:

        ele["slides"] = get_paraphrase(ele["slides"])
        ele["videos"] = get_paraphrase(ele["videos"])
        ele["experience"] = get_paraphrase(ele["experience"])
        answer.append(ele)

    with open("test.json", "w") as file:
        json.dump(answer, file, indent=2)