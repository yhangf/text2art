import re
import sys
import argparse

import PIL
import jieba
import requests
import numpy as np
from lxml import html
from wordcloud import WordCloud


def read_stopwords(file_path):
    stopwords = set()
    with open(file_path, 'rb') as fp:
        for line in fp.readlines():
            if not line.strip():
                continue
            stopwords.add(line.strip().decode('utf-8'))

    return stopwords

def get_html_text(url):
    response = requests.get(url)
    origin_text = response.text
    origin_text = re.sub(r'<script.*?>.*?</script>', '', origin_text, flags=re.I | re.M | re.DOTALL)
    origin_text = re.sub(r'<style.*?>.*?</style>', '', origin_text, flags=re.I | re.M | re.DOTALL)

    doc = html.fromstring(origin_text)
    text = doc.xpath('//body//text()')
    text = [i.strip() for i in text if i.strip()]
    text = ' '.join(text)
    seg = jieba.cut(text)

    stopwords = read_stopwords('./utils/stopwords.txt') # callable read_stopwords()
    seg = [i.strip() for i in seg if i.strip() and not i.strip().isdigit()
           and i.strip() not in stopwords]
    seg = ' '.join(seg)

    return seg

def get_txt(txt_file_path):
    with open(txt_file_path, 'r') as fp:
        txt_data = fp.read()
    words = list(jieba.cut(txt_data))
    words_list = [word for word in words if len(word)>1]
    word_join = ' '.join(words_list)

    return word_join

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', metavar='URL', default=None, help='input the url')
    parser.add_argument('--output', metavar='OUTPUT', default='./wordcloud.jpg', help='input the output_file')
    parser.add_argument('--input', metavar='INPUT_FIEL', default=None, help='input the input_file')
    parser.add_argument('--model', metavar='INPUT_IMAGE_MODEL', default=None, help='input the input_image_model')
    parser.add_argument('--ttf', metavar='INPUT_TTF', default='./font/simhei.ttf', help='input the typeface')
    parser.add_argument('--width', metavar='INPUT_WIDTH', default=1800, type=int, help='input the image width')
    parser.add_argument('--height', metavar='INPUT_HEIGHT', default=1000, type=int, help='input the image height')
    parser.add_argument('--bg', metavar='INPUT_BACKGROUND_COLOR', default='black', help='input the image background_color')
    parser.add_argument('--margin', metavar='INPUT_MARGIN', default=5, type=int, help='input the image margin')
    parser.add_argument('--max_font_size', metavar='INPUT_max_font_size', default=60, type=int, help='input the max_font_size')
    args = parser.parse_args()

    url = args.url
    output_file = args.output
    input_file = args.input
    model_path = args.model
    typeface = args.ttf
    max_font_size=args.max_font_size
    width = args.width
    height = args.height
    background_color = args.bg
    margin = args.margin

    try:
        image_mask = np.array(PIL.Image.open(model_path))
    except:
        image_mask=None

    wordcloud = WordCloud(font_path=typeface, mask=image_mask, max_font_size=max_font_size,
                          background_color=background_color, margin=margin, width=width, height=height)
    try:
        txt_join = get_txt(input_file)
        wordcloud_ = wordcloud.generate(txt_join)
    except:
        html_text = get_html_text(url)
        wordcloud_ = wordcloud.generate(html_text)

    image = wordcloud_.to_image()
    image.save(output_file)

if __name__ == '__main__':
    main()
