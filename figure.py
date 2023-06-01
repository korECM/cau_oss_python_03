"""
figure 모듈은 도형과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 이용하여 선의 길이를 설정하고 반환할 수 있으며,
area_rectangle, area_elipse, area_right_triangle 함수는
각각 직사각형, 타원, 직각삼각형의 넓이를 반환합니다.
"""
import math


class line:
    """
    line class는 선의 길이들에 대해 저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가능한 __witdh와 __height가 있으며,
    해당 변수를 수정하고 접근하기 위해
    set_length와, get_length 메소드를 제공합니다.
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """생성자 초기 width와 height 값을 입력
        Args:
            width (int or float): 선의 가로 길이
            height (int or float): 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        선의 길이를 수정
        Args:
            width (int or float): 수정하고자 하는 선의 가로 길이
            height (int or float): 수정하고자 하는 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """ 객체가 저장하고 있는 선의 길이를 반환
        Returns:
            int or float: 저장하고 있는 선의 길이
        """
        return self.__width, self.__height


def area_rectangle(width, height):
    """길이를 입력받아 직사각형의 넓이를 구하는 함수
    Args:
        width (int or float): 밑변의 길이
        height (int or float): 높이의 길이
    Returns:
        int or float: 직사각형의 넓이 값을 반환
    """
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height


def area_ellipse(width, height):
    """길이를 입력받아 타원의 넓이를 구하는 함수
    Args:
        width (int or float): 짧은 쪽 반지름의 길이
        height (int or float): 긴 쪽 반지름의 길이
    Returns:
        int or float: 타원의 넓이 값을 반환
    """
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height * math.pi


def area_right_triangle(width, height):
    """길이를 입력받아 직각삼각형의 넓이를 구하는 함수
    Args:
        width (int or float): 밑변의 길이
        height (int or float): 높이의 길이
    Returns:
        int or float: 직각삼각형의 넓이 값을 반환
    """
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height / 2
