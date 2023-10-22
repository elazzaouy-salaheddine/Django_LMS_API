from django.core.management.base import BaseCommand
from faker import Faker
from course.models import Quiz, Question, Choice, Module

class Command(BaseCommand):
    help = 'Generate fake quiz data'

    def add_arguments(self, parser):
        parser.add_argument('num_quizzes', type=int, help='Number of quizzes to create')
        parser.add_argument('num_questions', type=int, help='Number of questions per quiz')
        parser.add_argument('num_choices', type=int, help='Number of choices per question')

    def handle(self, *args, **kwargs):
        num_quizzes = kwargs['num_quizzes']
        num_questions = kwargs['num_questions']
        num_choices = kwargs['num_choices']
        modules = Module.objects.all()
        fake = Faker()

        for _ in range(num_quizzes):
            module = fake.random_element(elements=modules)
            quiz = Quiz.objects.create(
                module=module,
                title=fake.sentence(),
                description=fake.paragraph(),
                number_of_questions=num_questions,
                time_limit_minutes=fake.random_int(min=1, max=60),
                is_published=fake.boolean(chance_of_getting_true=50)
            )

            for _ in range(num_questions):
                question = Question.objects.create(
                    quiz=quiz,
                    question_text=fake.text()
                )

                for _ in range(num_choices):
                    is_correct = fake.boolean(chance_of_getting_true=30)
                    Choice.objects.create(
                        question=question,
                        choice_text=fake.word(),
                        is_correct=is_correct
                    )

        self.stdout.write(self.style.SUCCESS('Fake quiz data generated successfully.'))
