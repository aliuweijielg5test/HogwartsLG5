from test_frame_homework.app import App


class TestMarketPage:
    app = App()
    def test_market_page(self):
        self.app.start().goto_main().goto_market_page().goto_search_page().search()
