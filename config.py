
class BotOptions:
    TOKEN = ""
    ON_GAME = "모든 문의"
    OFF_GAME = "문의 일시정지"
    owner = ""
class NoQuestionMessage:
    TITLE = "문의가 일시정지 되어있습니다."
    MESSAGE = """안녕하세요. XXX 고객센터 입니다.
현제 문의를 받지 않고 있습니다.
`추후 다시 문의 바랍니다.`

지속적으로 문의를 받지 않는 다는 메시지가 뜰 경우,
Discord#0000 으로 문의바랍니다.

감사합니다.
"""
    AUTHOR = "새로운 미래로"
class FirstMessages:
    TITLE = "문의가 접수되었습니다."
    MESSAGE = """안녕하세요. XXX 문의센터 입니다.
__정상적으로 문의__ 가 전달되었습니다.
관리진이 확인후, 문의처리가 진행되오니 기다려 주시길 바랍니다.
최대 문의 처리시간은 `12시간 이내` 로 처리됩니다.

감사합니다.
"""
    AUTHOR = "XXX 서버 운영진"
class QuestionMessage:
    # %name% == 사용자 이름
    # %message% == 메시지
    MESSAGE = "%name%: %message%"
class AnswerMessage:
    # %top_role% == 최상의 역할 이름
    # %name% == 사용자 이름
    # %message% == 메시지
    #MESSAGE = "[ %top_role% ] %name%: %message%"
    MESSAGE = "[ %top_role% ]: %message%"
class CloseMessages:
    TITLE = "문의가 종료되었습니다."
    MESSAGE = """안녕하세요. XXX 문의센터 입니다.
관리진이 문의를 종료하였습니다.

해당메시지에 답변하지 말아주세요.

추후 문의가 있다면, 문의 바랍니다.
"""
    AUTHOR = "XXX 서버 운영진"
class OtherOptions:
    CATEGORY = 0
    LOG_CHANNEL = 0
    CLOSE_COMMAND = "!문의종료"
    ONOFF_COMMAND = "!문의"
    ON_MESSAGE = "문의 기능을 활성화 시켰습니다."
    OFF_MESSAGE = "문의 기능을 비활성화 시켰습니다."
class Emoji:
    FIRST = []
    MESSAGE  = "✅"
