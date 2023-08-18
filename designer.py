design = """
MDLabel:
    text: "Register"
    halign: "center"
    theme_text_color: "Primary"
    font_style: "H5"
"""
design = """
Screen:
    MDTextField:
        hint_text:"Username"
        helper_text :"should contain numbers and symbols"
        helper_text_color :"on_error"
        helper_text_mode:"on_focus"
        icon_right :"account"
        require:True
        pos_hint:{'center_x':.5,'center_y':.5}
        size_hint_x : None
        width:270
    
    MDTextField:
        hint_text:"Password"
        helper_text :"password should be greater than 8 char"
        helper_text_color :"on_error"
        helper_text_mode:"on_focus"
        icon_right:"eye"
        require:True
        pos_hint:{'center_x':.5,'center_y':.38}
        size_hint_x : None
        width:270
        password :True

    MDIconButton:
        icon : "google"
        pos_hint:{'center_x':.23,'center_y':.15}
    
    MDIconButton:
        icon : "facebook"
        pos_hint:{'center_x':.38,'center_y':.15}
    
    MDIconButton:
        icon : "instagram"
        pos_hint:{'center_x':.53,'center_y':.15}
    
    MDIconButton:
        icon : "twitter"
        pos_hint:{'center_x':.68,'center_y':.15}

"""