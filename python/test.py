from object import SampleObj

class ObjectSortTest:
    """
    Object내의 특정한 data를 기반으로 sorting하는 알고리즘 구현하기
    ------------------------------------------------------------
    검증 case:
    sorting에서 검증해야할 것은 무엇인가?
    string 오름차순 -> abc
    string 내림차순 -> cba
    int 오름차순, 내림차순
    기타 -> 순서의 기준이 되는 배열을 읽고 그에 맞춰 정렬
    """
    order_by_color = ["white, red, orange, yellow, green, blue, ocean, purple, black"]

    @staticmethod
    def assertEqual(data, compareTo):
        if data==compareTo:
            print("OK")
        else:
            print(f"FAIL. The expected value is {compareTo} but {data} is given")

    @staticmethod
    def assertTrue(cond):
        if cond:
            print("OK")
        else:
            print(f"FAIL the condition is false")

    @classmethod
    def run(cls, suite) -> None:
        print(cls.__doc__)
        count = 0
        for unit in suite:
            eval(f"cls.{unit}()")
            count += 1
        print(f"run ({count}) test")

    @classmethod
    def testObject(cls):
        o1 = SampleObj("Jone", 26, "white")
        o2 = SampleObj("Jone", 24, "red")
        cls.assertTrue(o1.name==o2.name)
        cls.assertEqual(o1.name, "James")
    
    @classmethod
    def test(cls):
        original = map(lambda x: x.name, objects)
        Collections.sort(objects, lambda x, y: x.name-y.name, sorted_by=1)
        new = map(lambda x: x.name, objects)
        cls.assertCompareIsTrue(original, new)

if __name__ == "__main__":
    suite = ["testObject"]
    ObjectSortTest.run(suite)
