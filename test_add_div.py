import pytest
import allure


@allure.feature("计算器")
class TestCal:

    # def setup_class(self):
    #     print("setup")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("teardown")
    @allure.story("相加-整数")
    @pytest.mark.run(order=1)
    def test_add_int(self, calc_class, get_add_calc):
        assert get_add_calc[2] == calc_class.add(get_add_calc[0], get_add_calc[1])

    @allure.story("相加-浮点数")
    @pytest.mark.run(order=2)
    def test_add_float(self, calc_class, get_add_calc1):
        assert get_add_calc1[2] == round(calc_class.add(get_add_calc1[0], get_add_calc1[1]), 2)

    @allure.story("相减-整数")
    @pytest.mark.run(order=6)
    def test_less_int(self, calc_class, get_less_calc):
        assert get_less_calc[2] == calc_class.less(get_less_calc[0], get_less_calc[1])

    @allure.story("相减-浮点数")
    @pytest.mark.run(order=8)
    def test_less_float(self, calc_class, get_less_calc1):
        assert get_less_calc1[2] == calc_class.less(get_less_calc1[0], get_less_calc1[1])

    @allure.story("相除-整数")
    @pytest.mark.run(order=7)
    def test_div_int(self, calc_class, get_div_calc):
        assert get_div_calc[2] == (calc_class.div(get_div_calc[0], get_div_calc[1]))

    @allure.story("相除-浮点数")
    @pytest.mark.run(order=5)
    def test_div_float(self, calc_class, get_div_calc1):
        assert get_div_calc1[2] == calc_class.div(get_div_calc1[0], get_div_calc1[1])

    @allure.story("相除-除数为0")
    @pytest.mark.run(order=4)
    def test_div_zero(self, calc_class, get_div_calc2):
        assert get_div_calc2[2] == calc_class.div(get_div_calc2[0], get_div_calc2[1])

    @allure.story("相乘-整数")
    @pytest.mark.run(order=9)
    def test_mul_int(self, calc_class, get_mul_calc):
        assert get_mul_calc[2] == calc_class.mul(get_mul_calc[0], get_mul_calc[1])

    @allure.story("相乘-浮点数")
    @pytest.mark.run(order=3)
    def test_mul_float(self, calc_class, get_mul_calc1):
        assert get_mul_calc1[1] == round(calc_class.mul(get_mul_calc1[0], get_mul_calc1[1]), 2)
