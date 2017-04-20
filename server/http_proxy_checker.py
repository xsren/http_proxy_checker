#coding:utf8
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/check_ip")
def check_ip():


    print request.remote_addr
    #print request.headers.keys()
    #print request.headers.values()
    for k,v in request.headers.iteritems():
        print '%s : %s \n' %(k,v)

    # if ',' in request.headers.get('X-Forwarded-For',""):
    #     p_type = u'使用了透明代理，真实IP：%s，代理IP：%s'%(request.headers['X-Forwarded-For'].split(',')[0],request.headers['X-Forwarded-For'].split(',')[1])
    # elif request.headers.has_key('Proxy-Connection'):
    #     p_type = u'使用普通匿名代理，代理地址：%s'%request.headers['X-Forwarded-For']
    # else:
    #     p_type = u'没有代理或使用了高匿代理，IP：%s'%request.headers['X-Forwarded-For']

    return "Hello World!"
    # return p_type

@app.route('/check_proxy')
def check_proxy():
    args = request.args
    self_ip = args.self_ip

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
