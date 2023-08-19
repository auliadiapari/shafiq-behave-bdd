class Locators:
    # BasePage
    URL = 'https://www.shafiq.id'
    # Homepage
    HOMEPAGE_NAVBAR = '//div[@class="navbar-collapse offcanvas-collapse'   # xpath
    HOMPAGE_DAFTAR_INVESTASI = 'Daftar Investasi'  # link text

    # Login
    LOGIN_GO_TO_LOGIN_PAGE = '//span[@class="text-h4 lg:text-h5"]'  # xpath
    LOGIN_FIELD_EMAIL = 'email'  # id
    LOGIN_FIELD_KATA_SANDI = 'password'  # id
    LOGIN_CLICK_BUTTON = '.\\[ > .text-h4'  # css
    # Dashboard
    SIDEBAR_DASHBOARD = 'li:nth-child(1)>a>span.side-shortcut__label'  # css
    SIDEBAR_PORTOFOLIO = 'li:nth-child(2)>a>span.side-shortcut__label'  # css
    SIDEBAR_DOMPET = 'li:nth-child(3)>a>span.side-shortcut__label'  # css
    SIDEBAR_PROFIL = 'li:nth-child(4)>a>span.side-shortcut__label'  # css
    SIDEBAR_BISNIS_SAYA = 'li:nth-child(5)>a>span.side-shortcut__label'  # css
    SIDEBAR_LAPORAN = 'li:nth-child(6)>a>span.side-shortcut__label'  # css
    SIDEBAR_BANTUAN = 'li:nth-child(7)>a>span.side-shortcut__label'  # css
    ALL_CAPTCHA = '.recaptcha-checkbox-border'  # css

    # Logout
    PROFILE_DROPDOWN = '.dropdown-toggle'  # css
    PROFILE_DROPDOWN_LOGOUT = 'Logout'  # link text

    # Forgot Password
    HOMEPAGE_NAVBAR_MASUK = '//div[@class="w-1/2 px-2 lg:px-1 lg:w-auto"]'  # xpath
    LUPA_KATA_SANDI_TXTLINK = '//a[@class="text-primary-light"]'  # xpath
    LUPA_KATA_SANDI_PGTITLE = '//span[@class="leading-tight text-h2 text-primary"]'  # xpath
    LUPA_KATA_SANDI_FIELD_EMAIL = 'email'  # name
    ALL_CAPTCHA = '.recaptcha-checkbox-border'  # css
    LUPA_KATA_SANDI_SUBMIT_BUTTON = '//span[@class="text-h4"]'  # xpath
    LUPA_KATA_SANDI_ALLERT = '.site-content' # css

    # Signup
    HOMEPAGE_MULAI_INVESTASI = '.home-slider'  # css
    SGNUP_AS_PERSONAL = '.col:nth-child(1) .w-full'  # css
    SGNUP_AS_CORPORATE = '//div[@class="col px-5"]'  # xpath
    SGNUP_PAGE_TITLE = '//span[@class="leading-tight text-h2 text-primary"]' # xpath

    SGNUP_FIELD_NAME = 'name'  # id
    SGNUP_FIELD_EMAIL = 'email'  # id
    SGNUP_FIELD_KATA_SANDI = 'password'  # id
    SGNUP_FIELD_KONFIRMASI_KATA_SANDI = 'confirm_password'  # id
    SGNUP_FIELD_SOURCE_INFO = 'choices--source_id-item-choice-13'  # id
    SGNUP_FIELD_SOURCE_NAME = 'source_name'  # id
    SGNUP_CLICK_BUTTON = '.form-submit-btn'  # css

    # Signup - Syarat dan Ketentuan Page
    TERMCONS_PAGE_TITLE = '//span[@class="leading-tight text-h2 text-primary"]'  # xpath
    TERMCONS_CHECKBOX = 'setuju'  # id
    TERMCONS_CLICK_BUTTON = '//div[@class="w-full pb-6 lg:md-0"'  # xpath
    TERMCONS_SGNUP_VERIF_MESSAGE = '//spanp[@class="text-h2 leading-tight"]'  # xpath

    # Daftar Investasi
    DFTAR_INVEST_PAGE_TITLE = '//span[@class="text-h3 text-primary font-light"]'  # xpath
    
    SORT_ICON = '.icon-sort'  # css
    SORTING_VALUE_1 = 'div:nth-child(2) > .p-filter > input' # css
    SORTING_VALUE_1 = 'div:nth-child(3) > .p-filter > input' # css
    SORTING_VALUE_1 = 'div:nth-child(4) > .p-filter > input' # css
    SORTING_VALUE_1 = 'div:nth-child(5) > .p-filter > input' # css
    SORTING_RESET = '#modal-sort-investasi .transparent-btn' # css
        
    FILTER_ICON = '.icon-filter'  # css
    FILTER_VALUE_1 = '.form-group:nth-child(1) .swiper-slide:nth-child(1) .cursor-pointer' # css
    FILTER_VALUE_2 = '.form-group:nth-child(2) .swiper-slide:nth-child(1) .cursor-pointer' # css
    FILTER_VALUE_3 = '.form-group:nth-child(3) .swiper-slide:nth-child(1) .cursor-pointer' # css
    FILTER_SUBMIT = '.btn-block > .text-secondary' # css
    FILTER_RESET = '#modal-filter-investasi .transparent-btn' # css
    
    SEARCH_BAR = 'search_keywords'  # Name
    SEARCH_ICON = '[type="text"]'  # CSS
    SEARCH_RESULT = '//div[@class="row"]' # xpath






  

  

    # # Login
    # LOGIN_GO_TO_LOGIN_PAGE = '//span[@class="text-h4 lg:text-h5"]'  # xpath
    # LOGIN_FIELD_EMAIL = 'email'  # id
    # LOGIN_FIELD_KATA_SANDI = 'password'  # id
    # LOGIN_CLICK_BUTTON = '.\\[ > .text-h4'  # css

    # # Dashboard
    # SIDEBAR_DASHBOARD = 'li:nth-child(1)>a>span.side-shortcut__label'  # css
    # SIDEBAR_PORTOFOLIO = 'li:nth-child(2)>a>span.side-shortcut__label'  # css
    # SIDEBAR_DOMPET = 'li:nth-child(3)>a>span.side-shortcut__label'  # css
    # SIDEBAR_PROFIL = 'li:nth-child(4)>a>span.side-shortcut__label'  # css
    # SIDEBAR_BISNIS_SAYA = 'li:nth-child(5)>a>span.side-shortcut__label'  # css
    # SIDEBAR_LAPORAN = 'li:nth-child(6)>a>span.side-shortcut__label'  # css
    # SIDEBAR_BANTUAN = 'li:nth-child(7)>a>span.side-shortcut__label'  # css

    # # Logout
    # PROFILE_DROPDOWN = '.dropdown-toggle'  # css
    # PROFILE_DROPDOWN_LOGOUT = 'Logout'  # link text

    # # Forgot Password
    # HOMEPAGE_NAVBAR_MASUK = '//div[@class="w-1/2 px-2 lg:px-1 lg:w-auto"]'  # xpath
    # LUPA_KATA_SANDI_TXTLINK = '//a[@class="text-primary-light"]'  # xpath
    # LUPA_KATA_SANDI_PGTITLE = '//span[@class="leading-tight text-h2 text-primary"]'  # xpath
    # LUPA_KATA_SANDI_FIELD_EMAIL = 'email'  # name
    # ALL_CAPTCHA = '.recaptcha-checkbox-border'  # css
    # LUPA_KATA_SANDI_SUBMIT_BUTTON = '//span[@class="text-h4"]'  # xpath
    # LUPA_KATA_SANDI_ALLERT = '.site-content' # css
