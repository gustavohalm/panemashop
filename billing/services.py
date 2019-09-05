from billing.models import Order
from django.conf import settings
from portal.models import UserProfile
from iugu.customer import Customer

from iugu.token import Token
class BillingServices(object):

    def create_remote_costumer(self, user):
        try:
            profile = user.userprofile
        except:
            profile = UserProfile()
            profile.user = user
            profile.save()

        if not profile.remote_costumer_id:
            data = {
                'email': user.email,
                'name': user.first_name + user.last_name,
            }
            customer = Customer()
            res = customer.create(data)
            if res['id']:
                user.userprofile.remote_costumer_id = res['id']
                user.userprofile.save()

        if user.userprofile.remote_costumer_id:
            print('yeahh')
            return user
        return False



    def charge(self, user, product, payment_data):
        remote_customer = self.create_remote_costumer(user)
        order = Order()
        order.user = product.user
        order.product = product
        order.total = product.price

        data = {
            'account_id': settings.IUGU_ACCOUNT_ID,
            'method':'credit_card',
            'test': 'true',
            'data': payment_data,
        }
        token = Token().create(data)
        print ( str( token ))
        if  'errors' in token:
            return False

        charge_data = {
            'token': token['id'],
            'costumer_id': user.userprofile.remote_costumer_id,
            'items': {
                'description': product.name,
                'quantity': 1,
                'price_cents': str(product.price ).replace('.', '')

            },
            'email': user.email,

        }
        charge = Token().charge( charge_data)

        if 'success' in charge:
            order = Order()
            order.product = product
            order.user = user
            order.merchant = product.user
            order.total = product.price
            order.status = 'Approved'
            order.save()
            return order

        return False
