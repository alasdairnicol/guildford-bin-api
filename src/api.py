import responder

api = responder.API()


@api.route('/v1/{day_of_week}/')
def hello_world(req, resp, day_of_week):
    day_of_week = day_of_week.title()
    resp.media = {'day_of_week': day_of_week}


if __name__ == "__main__":
    api.run()
