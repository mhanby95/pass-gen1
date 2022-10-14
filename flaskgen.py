from flask import Flask, render_template, request
app = Flask(str(__name__))
@app.route('/')
def passgen():
    
    import time
    import string




    for _ in range(10):
        lis = string.ascii_letters + string.digits
        pw = ''
        n = 6


        for i in range(n):
            y = time.time()
            savage = str(y).split('.')
            savage = str(int(savage[1]) % 7)
            

            if int(savage) <= 5 and i < n-1 :
                        idx = (int(savage)*10 + i) % len(lis)
                        pw += lis[idx]
            else:
                        idx = ((int(savage)-5)*10 + i) % len(lis)
                        pw += lis[idx]
        print(pw)

    return render_template('passgen.html', result=pw)


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.formr
        return render_template("result.html" ,result = result)

if __name__ == "_main_":
    app.run(debug = True)


