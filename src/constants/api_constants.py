# common path from API project and a class which contain all endpoints

# keep all urls

class ApiConstants(object):

    def base_url(self):

        return "https://restful-booker.herokuapp.com/"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    #update, put, patch, Delete -booking_id

    def url_put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

