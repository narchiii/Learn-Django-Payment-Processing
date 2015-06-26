from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		
		# Create the charge on Stripe's servers - this will charge the user's card
		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(card=token)
  			charge = stripe.Charge.create(
      			amount=1000, # amount in cents, again
      			currency="usd",
      			customer=customer,
      			description="payinguser@example.com"
  				)
		except stripe.CardError, e:
  			# The card has been declined
  			pass
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request, template, context)