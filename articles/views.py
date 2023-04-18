from rest_framework import status
# HTTP STATUS CODE를 사용하기 위한 헤더, 연결상태를 전송할 수 있다.
from rest_framework.response import Response
# HTTP Resonse처럼, 어떠한 데이터를 전송할 수 있다.
from rest_framework.decorators import api_view
# api_view 데코레이터 헤더, GET,POST,PUT,DELETE요청을 제어할 수 있다.
from rest_framework.generics import get_object_or_404
# 지금까지 사용했던 모델의 데이터 탐색 방법은
# 모델.objects.get(id=id)의 방식을 사용했는데, 이때 탐색값이 없다면 DoesNotExist에러가 발생했다.
# get_object_or_404는 이름 그대로 object를 받거나, 404에러를 처리할 수 있다.
from .models import Articles
# 사용자가 정의한 model
from .serializers import SerializerArticle
# 사용자가 정의한 serializers model

@api_view(['GET','POST'])
# api_view 데코레이터를 사용함으로써, GET,POST 요청을 다룰 수 있다.
def articleAPI(request):
    if request.method == 'GET':
        articles_data = Articles.objects.all()
        articles = SerializerArticle(articles_data,many=True)
        # 쿼리로 뽑아낸 데이터를 JSON 형태로 묶어준다. 이때 many는 하나의 데이터가 아닌 여러개의 데이터인점을 알린 것
        return Response(articles.data)
        # 지금까지 context나 딕셔너리 형태를 그대로 반환했지만. 이제 .(dot)data를 붙여줘야 한다.
    elif request.method == 'POST':
        serializer = SerializerArticle(data = request.data)
        # 전송된 데이터를 가공하여 변수에 저장(필드)
        if serializer.is_valid():
            # 유효성 검사를 자동으로 해준다.
            serializer.save()
            # 데이터 저장
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            # 저장한 데이터를 출력시키기 위한 코드, 201상태와 함께 반환한다.
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # 에러창은 보안상 관계로 개발환경에서만 사용하는것이 적합합다.

@api_view(['GET','PUT','DELETE'])
# form과 달리 API는 PUT,PETCH,DELETE를 사용할 수 있다.
# PUT은 데이터 전체를 필요로하는 반면 , PETCH는 데이터 일부만을 필요로하고, 둘다 UpDate에 적합하다.
def articleDetailAPI(request,article_id):
    #상세 페이지
    if request.method == 'GET':
        article = get_object_or_404(Articles,id=article_id)
        # Articles모델에서 id값을 비교한다, 데이터가 없다면 404 에러를 담는다.
        serializer = SerializerArticle(article)
        # 탐색한 데이터를 변수에 저장
        return Response(serializer.data)
    elif request.method =='PUT':
        article = get_object_or_404(Articles,id=article_id)
        # Article 모델의 id값에 해당하는 object 탐색
        serializer = SerializerArticle(article,data=request.data)
        # object article 의 데이터를 변경한 내역을 변수에 저장
        if serializer.is_valid():
            # 유효성 검사후 저장
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article = get_object_or_404(Articles, id=article_id)
        #Articles 모델에서 id값에 해당하는 object를 탐색 후 데이터 삭제
        article.delete()

        return Response(status=status.HTTP_404_NOT_FOUND)