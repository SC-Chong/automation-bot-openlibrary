from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_language(language='English')
    bot.search_books('Harry Potter')
    bot.click_search()
    bot.apply_filtrations(language_chosen='English')
    bot.refresh()  #a workaround to let bot grab data properly
    bot.report_results()
    