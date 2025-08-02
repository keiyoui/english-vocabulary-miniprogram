from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
import random
import uuid
from .models import TestRecord, Question
from .serializers import QuestionSerializer, TestRecordSerializer, TestSubmitSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_questions(request):
    """获取测试题目"""
    test_type = request.GET.get('test_type', 'vocabulary')
    difficulty = request.GET.get('difficulty', 'intermediate')
    question_count = int(request.GET.get('question_count', 20))
    
    # 根据条件筛选题目
    questions = Question.objects.filter(
        is_active=True,
        difficulty=difficulty
    ).order_by('?')[:question_count]
    
    serializer = QuestionSerializer(questions, many=True)
    
    return Response({
        'questions': serializer.data,
        'test_id': str(uuid.uuid4()),
        'total_count': len(serializer.data)
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_test(request):
    """提交测试答案"""
    serializer = TestSubmitSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    test_id = data['test_id']
    answers = data['answers']
    duration = data['duration']
    
    # 计算得分
    correct_count = 0
    total_questions = len(answers)
    
    for answer in answers:
        question_id = answer.get('question_id')
        user_answer = answer.get('answer')
        
        try:
            question = Question.objects.get(id=question_id)
            if question.correct_answer == user_answer:
                correct_count += 1
        except Question.DoesNotExist:
            continue
    
    score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    
    # 确定词汇水平
    if score >= 90:
        vocabulary_level = 'advanced'
    elif score >= 70:
        vocabulary_level = 'intermediate'
    else:
        vocabulary_level = 'beginner'
    
    # 创建测试记录
    test_record = TestRecord.objects.create(
        user=request.user,
        test_type='vocabulary',
        difficulty='intermediate',
        total_questions=total_questions,
        correct_answers=correct_count,
        score=score,
        vocabulary_level=vocabulary_level,
        duration=duration,
        start_time=timezone.now() - timezone.timedelta(seconds=duration),
        end_time=timezone.now()
    )
    
    # 更新用户统计
    user = request.user
    user.total_tests += 1
    user.vocabulary_level = vocabulary_level
    
    # 计算新的平均分数
    total_score = user.average_score * (user.total_tests - 1) + score
    user.average_score = total_score / user.total_tests
    user.save()
    
    return Response({
        'test_id': test_record.id,
        'score': score,
        'correct_count': correct_count,
        'total_questions': total_questions,
        'vocabulary_level': vocabulary_level
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_test_result(request, test_id):
    """获取测试结果"""
    try:
        test_record = TestRecord.objects.get(id=test_id, user=request.user)
        serializer = TestRecordSerializer(test_record)
        return Response(serializer.data)
    except TestRecord.DoesNotExist:
        return Response({'error': '测试记录不存在'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_test_history(request):
    """获取测试历史"""
    test_type = request.GET.get('test_type')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    
    queryset = TestRecord.objects.filter(user=request.user)
    
    if test_type:
        queryset = queryset.filter(test_type=test_type)
    
    if date_from:
        queryset = queryset.filter(created_at__gte=date_from)
    
    if date_to:
        queryset = queryset.filter(created_at__lte=date_to)
    
    serializer = TestRecordSerializer(queryset, many=True)
    return Response({'results': serializer.data}) 