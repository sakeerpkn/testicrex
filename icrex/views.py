

import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


def fetch_resources(uri, rel):
    path = os.path.join(settings.STATIC_URL, uri.replace(settings.STATIC_URL, ""))
    print "fetch_resources==", path
    return path
    



def web_render_to_pdf(template_src,context_dict):
    html = get_template(template_src).render(context_dict)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('utf-8') ),  dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        response['message'] = 'Failed: '+str(pdf.err)+' '
    return HttpResponse(json.dumps(response), content_type="application/json")


def icrex_pdf_1(request):
    results = []
    html = 'pdf_template-1.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_2(request):
    results = []
    html = 'pdf_template-2.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_3(request):
    results = []
    html = 'pdf_template-3.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_4(request):
    results = []
    html = 'pdf_template-4.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def test(request):
    from django.shortcuts import render

    return render(request, 'pdf_template-2.html')

################################API STARTS HERE #####################


def api_render_to_pdf(response,template_src):
    html = template_src
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('utf-8') ),  dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        response['message'] = 'Failed: '+str(pdf.err)+' '
    return HttpResponse(json.dumps(response), content_type="application/json")


@csrf_exempt
def icrex_pdf_api(request):
    # request_data = request.body.decode('utf-8')
    results = []
    response = {}
    response['status_code'] = 500
    response['message'] = 'Failed'
    try:
        if 'html' in request.body:
            import ast
            data = ast.literal_eval(request.body)
            html = data['html']
            return api_render_to_pdf(
                response,
                html,
            )
        else:
            response['message'] = 'Missing arguments in json data'
            print "noooooooo"
    except Exception as e:
        print "Exception===", e
        response['message'] = 'Failed: '+str(e)+' '
    print "response", response
    return HttpResponse(json.dumps(response), content_type="application/json")