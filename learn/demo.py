import atheris
import sys

with atheris.instrument_imports():
    pass


@atheris.instrument_func
def TestOneInput(data):
    # if len(data) < 4:
    #     return
    # print("---------------------")
    # print(f"data bytes: {data}")
    # print(f"len(data): {len(data)}")

    fdp = atheris.FuzzedDataProvider(data)

    ## 生成多少个字节

    # print(f"ConsumeBytes: {fdp.ConsumeBytes(4)}")

    ## 生成Unicode字符串

    # # 由于 fdp.ConsumeUnicode(4) 返回的字符串可能包含了代理对（surrogates），
    # # 而这些字符在默认的 utf-8 编码中是不允许的（不能直接print）。
    # # 为了避免这个问题，你可以在打印之前对字符串进行处理，或者使用 repr 函数来显示字符串的原始表示。
    # print(f"ConsumeUnicode: {repr(fdp.ConsumeUnicode(4))}")
    # print(f"ConsumeUnicodeNoSurrogates: {repr(fdp.ConsumeUnicodeNoSurrogates(4))}")
    # print(f"ConsumeString: {fdp.ConsumeString(4)}")

    ## 生成整数

    # print(f"ConsumeInt: {fdp.ConsumeInt(4)}")
    # if fdp.ConsumeInt(4) == 13456:
    #     raise ValueError("ConsumeInt: 13456")
    # if fdp.ConsumeInt(4) == -43216:
    #     raise ValueError("ConsumeInt: -43216")

    # print(f"ConsumeUInt: {fdp.ConsumeUInt(4)}")
    # if fdp.ConsumeUInt(4) == 64781:
    #     raise ValueError("ConsumeUInt is 64781")

    # print(f"ConsumeIntInRange: {fdp.ConsumeIntInRange(0, 100)}")
    # if fdp.ConsumeIntInRange(0, 100) == 23:
    #     raise ValueError("ConsumeIntInRange is 23")

    # print(f"ConsumeIntList: {fdp.ConsumeIntList(2,2)}")
    # if fdp.ConsumeIntList(2, 4) == [712, 234]:  # 这种很难触发
    #     raise ValueError("ConsumeIntList is [712,234]")

    # print(f"ConsumeIntListInRange: {fdp.ConsumeIntListInRange(2,0,100)}")

    ## 生成浮点数

    # print(f"ConsumeFloat: {fdp.ConsumeFloat()}")

    # data = fdp.ConsumeRegularFloat()
    # if data > 200000000:
    #     return
    # elif data < 2:
    #     return
    # else:
    #     raise ValueError("ConsumeRegularFloat is 2.5")
    # print(f"ConsumeRegularFloat: {fdp.ConsumeRegularFloat()}")

    # 生成0-1之间的浮点数
    # print(f"ConsumeProbability: {fdp.ConsumeProbability()}")

    # print(f"ConsumeFloatInRange: {fdp.ConsumeFloatInRange(0, 100)}")

    # print(f"ConsumeFloatList: {fdp.ConsumeFloatList(2)}")

    # print(f"ConsumeRegularFloatList: {fdp.ConsumeRegularFloatList(2)}")

    # print(f"ConsumeProbabilityList: fdp.ConsumeProbabilityList(2)")

    # print(f"ConsumeFloatListInRange: {fdp.ConsumeFloatListInRange(2, 0, 100)}")

    # 从列表中随机选择一个元素
    # l = [1, 2, 3, 4, 5]
    # print(f"PickValueInList: {fdp.PickValueInList(l)}")

    ## 生成布尔值

    # print(f"ConsumeBool: {fdp.ConsumeBool()}")


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
