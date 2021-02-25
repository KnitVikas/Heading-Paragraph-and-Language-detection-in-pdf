from collections import Counter
import re
import spacy
from spacy_langdetect import LanguageDetector
from collections import Counter
from utils import detect_para

nlp = spacy.load("en")
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


def main(path):

    paragraph = []
    heading = []
    lang = []

    try:
        elements = detect_para(path)
        # print(elements)
        for i in elements:
            # print(i)
            if (
                i.startswith("<h1>")
                or i.startswith("<h2>")
                or i.startswith("<h3>")
                or i.startswith("<h4>")
            ):
                heading.append(i.split(">")[1].replace("|", ""))

                text = re.sub("[^a-zA-Z]", " ", i)
                if text:
                    doc = nlp(text)
                    lang.append(doc._.language["language"])
                else:
                    print("missing text in sentence")

            elif i.startswith("<p>") or i.startswith("<s1>"):
                paragraph.append(i.split(">")[1].replace("|", ""))

                text = re.sub("[^a-zA-Z]", " ", i)
                if text:
                    doc = nlp(text)
                    lang.append(doc._.language["language"])
                else:
                    print("missing text in sentence")
            else:
                print("This is not useful text in document")
                pass
        paragraph = " ".join(paragraph)
        heading = " ".join(heading)
        print("Language detected is : ", most_frequent(lang))
        print("Heading text detected is : ", heading)
        print("Paragraph text detected is : ", paragraph)
    except:
        print("Nothing useful detected.")


if __name__ == "__main__":

    path = "Chinese-Traditional-Fathers-Love-Letter.pdf"
    main(path)