
from django.conf.urls import url
from views import  icrex_pdf_1,icrex_pdf_2,icrex_pdf_3,icrex_pdf_4, icrex_pdf_5,\
	icrex_pdf_6, icrex_pdf_7, icrex_pdf_8, icrex_pdf_api, test
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'', icrex_pdf_1),
    url(r'^template-render-1/', icrex_pdf_1),
    url(r'^template-render-2/', icrex_pdf_2),
    url(r'^template-render-3/', icrex_pdf_3),
    url(r'^template-render-4/', icrex_pdf_4),
    url(r'^template-render-5/', icrex_pdf_5),
    url(r'^template-render-6/', icrex_pdf_6),
    url(r'^template-render-7/', icrex_pdf_7),
    url(r'^template-render-8/', icrex_pdf_8),

    url(r'^pdf-report-api', icrex_pdf_api),

    url(r'^test/', test),
    
    
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)