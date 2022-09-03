class messages:
    """
    params: language: str = 'en' | 'fa'. default: 'en'
    response: {'status': bool, 'code': str, 'message': str}
    Example of usage:
        from base_fastapi_utils.api.core.messages import messages
        messages('en').ERR_MORE_THAN_N_TRY(config.MAX_NUMBER_OF_TRY, cellnum, status: bool (default=false))
    """

    def __init__(self, language: str = 'en'):
        self.language = language

    def ERR_FAILED_TO_CONNECT_TO_SERVER(self, status: bool = False):
        if self.language == 'fa':
            msg = "خطا در اتصال به سرور"
        else:
            msg = "Failed to connect to server"
        return {'status': status,
                'code': "E100",
                'message': msg}

    def ERR_FAILED_TO_CONNECT_TO_DATABSE(self, status: bool = False):
        if self.language == 'fa':
            msg = "خطا در اتصال به پایگاه داده"
        else:
            msg = "Failed to connect to database"
        return {'status': status,
                'code': "E101",
                'message': msg}

    def ERR_TRY_AGAIN(self, status: bool = False):
        if self.language == 'fa':
            msg = "لطفا دوباره تلاش کنید"
        else:
            msg = "Please try again"
        return {'status': status,
                'code': "E102",
                'message': msg}

    def ERR_TRY_AGAIN_LATER(self, status: bool = False):
        if self.language == 'fa':
            msg = "لطفاً بعداً دوباره امتحان کنید"
        else:
            msg = "Please try again later"
        return {'status': status,
                'code': "E103",
                'message': msg}

    def ERR_DB_LOCKED(self, status: bool = False):
        if self.language == 'fa':
            msg = "پایگاه داده قفل است"
        else:
            msg = "Database locked"
        return {'status': status,
                'code': "E104",
                'message': msg}

    def ERR_USERNAME_OR_PASSWORD_IS_WRONG(self, status: bool = False):
        if self.language == 'fa':
            msg = "نام کاربری یا کلمه عبور اشتباه است"
        else:
            msg = "Username or password is wrong"
        return {'status': status,
                'code': "E105",
                'message': msg}

    def ERR_WRONG_PARAMS(self, parameter: str, status: bool = False):
        if self.language == 'fa':
            msg = "پارامتر %s صحیح نیست" % parameter
        else:
            msg = f"{parameter} parameter is wrong"
        return {'status': status,
                'code': "E106",
                'message': msg}

    def ERR_CUSTOM(self, msg: str, status: bool = False):
        return {'status': status,
                'code': "E107",
                'message': msg}

    def ERR_NOT_FOUND(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s یافت نشد" % username
        else:
            msg = "%s not found" % username
        return {'status': status,
                'code': "E200",
                'message': msg}

    def ERR_WRONG_OR_NOT_EXIST(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s اشتباه است یا وجود ندارد" % username
        else:
            msg = "%s is wrong or not exist" % username
        return {'status': status,
                'code': "E201",
                'message': msg}

    def ERR_FAILED_TO_CREATE(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s اضافه نشد. از قبل موجود است" % username
        else:
            msg = "Failed to add %s. Already exist" % username
        return {'status': status,
                'code': "E202",
                'message': msg}

    def ERR_FAILED_TO_UPDATE(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s به روز نشد" % username
        else:
            msg = "Failed to update %s" % username
        return {'status': status,
                'code': "E203",
                'message': msg}

    def ERR_FAILED_TO_DELETE(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s حذف نشد" % username
        else:
            msg = "Failed to delete %s" % username
        return {'status': status,
                'code': "E204",
                'message': msg}

    def ERR_MORE_THAN_N_TRY(self, count: int, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "بیش از %d تلاش برای %s" % (count, username)
        else:
            msg = "More than %d try for %s" % (count, username)
        return {'status': status,
                'code': "E300",
                'message': msg}

    def ERR_NOT_ENABLE(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s فعال نیست" % username
        else:
            msg = "%s is not enable" % username
        return {'status': status,
                'code': "E301",
                'message': msg}

    def ERR_NOT_VERIFIED(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s تایید نشده است" % username
        else:
            msg = "%s not verified" % username
        return {'status': status,
                'code': "E302",
                'message': msg}

    def ERR_EXPIRED(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "حساب %s منقضی شده است" % username
        else:
            msg = "%s account has expired" % username
        return {'status': status,
                'code': "E303",
                'message': msg}

    def ERR_NOT_STARTED(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "حساب %s هنوز فعال نشده است" % username
        else:
            msg = "%s account has not started yet" % username
        return {'status': status,
                'code': "E304",
                'message': msg}

    def ERR_NO_RECORD_IN_OTP_OR_TIMEOUT(self, username: str, status: bool = False):
        if self.language == 'fa':
            msg = "درخواست کد برای %s ثبت نشده یا منقضی شده است" % username
        else:
            msg = "No OTP request exist for %s or Timeout" % username
        return {'status': status,
                'code': "E305",
                'message': msg}

    def ERR_WRONG_CODE(self, code: str, status: bool = False):
        if self.language == 'fa':
            msg = "%s اشتباه است" % code
        else:
            msg = "%s is wrong" % code
        return {'status': status,
                'code': "E306",
                'message': msg}

    def ERR_NO_CELLNUM_WITH_OTP(self, cellnum: str, otp: str, status: bool = False):
        if self.language == 'fa':
            msg = "شماره %s با کد %s مطابقت ندارد" % (cellnum, otp)
        else:
            msg = "%s doesn't match with code %s" % (cellnum, otp)
        return {'status': status,
                'code': "E307",
                'message': msg}

    def INF_SUCCESS(self, status: bool = True):
        if self.language == 'fa':
            msg = "موفق"
        else:
            msg = "success"
        return {'status': status,
                'code': "S100",
                'message': msg}

    def INF_SUCCESS_BY_ADMIN(self, status: bool = True):
        if self.language == 'fa':
            msg = "موفق با دسترسی ادمین"
        else:
            msg = "success by admin access"
        return {'status': status,
                'code': "S101",
                'message': msg}

    def INF_OTP_SENT_TO(self, cellnum: str, status: bool = True):
        if self.language == 'fa':
            msg = "کد به %s ارسال شد" % cellnum
        else:
            msg = "OTP sent to %s" % cellnum
        return {'status': status,
                'code': "S300",
                'message': msg}

    def INF_SUCCESS_GET_ANSWER_FROM_SINA(self, status: bool = True):
        if self.language == 'fa':
            msg = "موفق"
        else:
            msg = "successfull"
        return {'status': status,
                'code': "S102",
                'message': msg}

    def ERR_NOT_CONNECT_TO_SINA(self,  status: bool = False):
        if self.language == 'fa':
            msg = "خطا در برقراری ارتباط با سرور سینا"
        else:
            msg = "Failed to connect to the SINA server"
        return {'status': status,
                'code': "E307",
                'message': msg}


    def INF_ERROR_GET_ANSWER_FROM_SINA(self,  status: bool = False):
        if self.language == 'fa':
            msg = "پاسخ خالی از سرور سینا دریافت شد"
        else:
            msg = "Empty answer received from SINA"
        return {'status': status,
                'code': "E308",
                'message': msg}
    def INF_ERROR_CHAT_ROOM(self,  status: bool = False):
        if self.language == 'fa':
            msg = "چت روم انتخاب شده در لیست نمی باشد"
        else:
            msg = "Wrong Chatroom Name"
        return {'status': status,
                'code': "E309",
                'message': msg}
    def INF_ERROR_STATUS_CODE_ANSWER_FROM_SINA(self,  status: bool = False):
        if self.language == 'fa':
            msg = "استتوس کد دریافتی از سرور مخالف ۲۰۰ است: "
        else:
            msg = " The status code from the server is not 200, that is:   "
        return {'status': status,
                'code': "E310",
                'message': msg}
