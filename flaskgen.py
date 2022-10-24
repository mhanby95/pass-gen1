from flask import Flask, render_template, request
app = Flask(str(__name__))

def Swap_Case(xyz):
    str_value = ""
    for word in xyz:
        if word.isupper():
            str_value += word.lower()
        else:
            str_value += word.upper()
    return str_value


@app.route('/')
def passgen():
    import time
    import string

    for _ in range(10):
        lis = string.digits + str({'word list.txt'})
        pw = ''
        n = 5
        lis = []
        for i in range(n):
            y = time.time()
            savage = str(y).split('.')
            lis.append(str((int(savage[1]) % 5) + 1))
        
        with open('word list.txt', 'r') as f:
            lines = f.readlines()
            num = int(''.join(lis))
            for line in lines:
                if str(num) in line:
                    print(line.split()[0])


        print(pw)

    return render_template('passgen.html', result=pw)


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.formr
        return render_template("result.html" ,result = result)

@app.route('/swapcase',methods = ['POST', 'GET'])
def swapcase():
    # if request.method == 'POST':
    result = Swap_Case("BlasdklfjaslkdfbLIHSDOFIN")
    return result

@app.route('/6174',methods = ['POST', 'GET'])
def d6174():
    # if request.method == 'POST':
    result = request.form

    result = Swap_Case("BlasdklfjaslkdfbLIHSDOFIN")
    return result


if __name__ == "__main__":
    app.run(debug = True)
      



