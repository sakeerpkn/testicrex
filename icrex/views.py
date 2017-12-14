

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
    print "===================================================================11"
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
    print "===================================================================22"
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
    print "===================================================================33"
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
    print "===================================================================44"
    results = []
    html = 'pdf_template-4.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_5(request):
    print "===================================================================55"
    results = []
    html = 'pdf_template-5.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_6(request):

    print "===================================================================66"
    results = []
    html = 'pdf_template-6.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_7(request):
    print "===================================================================77"

    results = []
    html = 'pdf_template-7.html'
    return web_render_to_pdf(
            html,
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def icrex_pdf_8(request):
    print "===================================================================88"
    results = []
    html = 'pdf_template-8.html'
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





def api_render_to_single_pdf(response,template_src):
    print "api_render_to_single_pdf"
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(template_src),  dest=result, encoding='utf-8' )
    if not pdf.err:
        print "no error"
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        print "its error"
        response['message'] = 'Failed: '+str(pdf.err)+' '
    return HttpResponse(json.dumps(response), content_type="application/json")


@csrf_exempt
def icrex_pdf_api(request):
    print "===================================================================api single"
    import ast
    import json

    results = []
    response = {}
    response['status_code'] = 500
    response['message'] = 'Failed'
    try:
        if 'html' in request.body:
            data = ast.literal_eval(request.body)
            html = data['html']

            return api_render_to_single_pdf(
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


def delete_all_existing_files():
    import os, shutil
    folder = 'templates/pdfs/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def api_render_to_multiple_pdf(response,template_src,pdf_array):
    import uuid
    filename = str(uuid.uuid4())
    result = open('templates/pdfs/'+str(filename), "w+b")
    pdf = pisa.CreatePDF(StringIO.StringIO(template_src),  dest=result, encoding='utf-8' )
    if not pdf.err:
        print "created", pdf_array
        pdf_array.append('templates/pdfs/' + filename)
    else:
        response['message'] = 'Failed: '+str(pdf.err)+' '
        return HttpResponse(json.dumps(response), content_type="application/json")


@csrf_exempt
def icrex_multiple_pdf_api(request):
    print "===================================================================api multiple"
    import ast
    import json
    pdf_array = []
    results = []
    response = {}
    response['status_code'] = 500
    response['message'] = 'Failed'
    try:
        delete_all_existing_files()
        if 'html' in request.body:
            data = json.loads(request.body)
            html_array = data["html"]
            for html in html_array:
                api_render_to_multiple_pdf(
                    response,
                    html,
                    pdf_array
                )
            else:
                from PyPDF2 import PdfFileMerger
                merger = PdfFileMerger()
                for pdfs in pdf_array:
                    merger.append(pdfs)
                result = StringIO.StringIO()
                merger.write(result)
                return HttpResponse(result.getvalue(), content_type='application/pdf')
        else:
            response['message'] = 'Missing arguments in json data'
    except Exception as e:
        print "Exception===", e
        response['message'] = 'Failed: '+str(e)+' '
    print "response", response
    return HttpResponse(json.dumps(response), content_type="application/json")