from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from setfit import SetFitModel

class AnalyzeView(APIView):
    def post(self, request):
        # Retrieve the text from the POST request payload
        text = request.data.get('text')

        # Perform sentiment analysis using the SetFitModel
        model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
        preds = model([text])

        # Determine the sentiment label
        sentiment_label = preds[0]

        # Map the SetFitModel's labels to positive, negative, or neutral
        # sentiment_map = {
        #     '1': 'negative',
        #     '2': 'neutral',
        #     '3': 'positive'
        # }
        # sentiment = sentiment_map.get(sentiment_label, 'unknown')

        if sentiment_label < 0.5:
            sentiment = 'negative'
        elif sentiment_label > 0.5:
            sentiment = 'postitive'

        # Create the JSON response
        response_data = {
            'sentiment': sentiment
        }

        return Response(response_data)
    
class IndexView(TemplateView):
    template_name = 'index.html'

