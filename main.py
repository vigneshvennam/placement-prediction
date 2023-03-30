from flask import Flask,request,jsonify,render_template,redirect,url_for
import util
app=Flask(__name__)


@app.route('/result<int:score>')
def result(score):
   
    if score==0:
        res="SERVICE"
    else:
        res="PRODUCT"
    return render_template('res.html',result=res)


   


@app.route('/')
def hello():
    return render_template('app.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        eng=float(request.form['eng'])
        qa=float(request.form['qa'])
        la=float(request.form['la'])
        cp=float(request.form['cp'])
        essay=float(request.form['essay'])
        core=float(request.form['core'])
    #global predicted_company
    #response=jsonify({
        #util.load_saved_artifects()
        #'predicted_company':int(util.get_company(eng,qa,la,cp,auto,autofix,essay))

    #})
    #response.header.add("Access-Control-Allow-Origin",'*')
    #return redirect(url_for('submit',score=response.))
    #return response
    #data=request.get_json()
    #x=data['predicted_company']
    predicted_company=int(util.get_company(eng,qa,la,cp,essay,core))
    return redirect(url_for('result',score=predicted_company))
    


if __name__=="__main__":
    app.run()
