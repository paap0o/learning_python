def response(hey_bob):
    remark = hey_bob.strip()

    if not remark : 
        return 'Fine. Be that way!'

    is_yelling = remark.isupper()
    is_question = remark.endswith("?")

    if is_yelling and is_question : 
        return 'Calm down, I know what I\'m doing!'

    if is_yelling:
        return 'Whoa, chill out!'

    if is_question : 
        return 'Sure.'

    else : 
        return 'Whatever.'

    
