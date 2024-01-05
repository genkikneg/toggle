from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

mojiretu = {"mojiretu":"firstnumber"}

def combineStrNum(moji, num):
    if moji == "firstnumber":
        combined_result = str(num)
    else:
        combined_result = str(moji) + str(num)
    outputDic = {"mojiretu":combined_result}
    return outputDic

def toggle(str):
    print(str)
    alphabet = [
        ['.', ',', '!', '?', ' '],['a', 'b', 'c'],['d', 'e', 'f'],
        ['g', 'h', 'i'],['j', 'k', 'l'],['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']
    ]

    count = 0
    index = 3

    outputDic = {"mojiretu":""}
    for i in range(len(str) - 1):
        if str[i + 1] == str[i] and str[i] != '0':
            count += 1
        elif str[i] != '0':
            fig = int(str[i])
            if fig in [7, 9]:
                index = 4
            elif fig == 1:
                index = 5

            print(alphabet[fig - 1][count % index], end='')
            changedToStr = []
            changedToStr.append(alphabet[fig - 1][count % index])
            outputStr = "".join(changedToStr)
            count = 0
            index = 3
            outputDic['mojiretu'] += outputStr
    return outputDic

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', message='出力')
    
@app.route('/form', methods=['GET'])
def form():
    global mojiretu

    button = request.args.get('button')
    if request.method == 'GET':
        if button != "Enter":
            #末尾を消去
            if button == "X":
                mojiretu['mojiretu'] = mojiretu['mojiretu'][:-1]
            else:
                mojiretu = combineStrNum(str(mojiretu['mojiretu']), button)
            print("入力値{}".format(mojiretu['mojiretu']))
            outputDic = toggle(mojiretu['mojiretu'])
            return render_template('home.html', message=outputDic['mojiretu'], numberName=mojiretu['mojiretu'])
        else:
            outputDic = toggle(mojiretu['mojiretu'])
            return render_template('home.html', message=outputDic['mojiretu'])

if __name__ == "__main__":
    app.run()
