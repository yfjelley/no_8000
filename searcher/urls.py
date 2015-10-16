from django.conf.urls import patterns, url

urlpatterns = patterns('searcher.views',
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^$', 'index', name='searchindex'),
    url(r'^login/$',  'login', name='login'),
    url(r'^logout/$',  'logout', name='logout'),
    url(r'^register/$',  'register', name='register'),
    url(r'^add_favoritebid/(?P<objectid>\d+)/$',  'add_favoritebid', name='add_favoritebid'),
    url(r'^add_favoriteplatform/(?P<objectid>\d+)/$',  'add_favoriteplatform', name='add_favoriteplatform'),
    url(r'^add_reminder/(?P<objectid>\d+)/$',  'add_reminder', name='add_reminder'),
    url(r'^del_reminder/(?P<objectid>\d+)/$',  'del_reminder', name='del_reminder'),
    url(r'^do_reminder/$',  'do_reminder', name='do_reminder'),
    url(r'^myfavorite/(?P<tid>\d+)/$$',  'myfavorite', name='myfavorite'),
    url(r'^platform/$',  'platform', name='platform'),
    url(r'^userinformation/$',  'userinformation', name='userinformation'),
    url(r'^save_filter/$',  'save_filter', name='save_filter'),
    url(r'^del_filter/(?P<fid>\d+)/$',  'del_filter', name='del_filter'),
    url(r'^bid_detail/(?P<objectid>\d+)/$',  'bid_detail', name='bid_detail'),
    url(r'^bid_detail_p/$',  'bid_detail_p', name='bid_detail_p'),

    url(r'^comb_detail/(?P<ids>[^/]+)/$',  'comb_detail', name='comb_detail'),
    url(r'^shortcut_request/(?P<objectid>\d+)/$',  'shortcut_request', name='shortcut_request'),
    url(r'^getverifycode/$', 'verifycode', name='verifycode'),
    url(r'^forgetpw/$', 'forgetpw', name='forgetpw'),
    # url(r'^other_page_reg/$',  'other_page_reg', name='other_page_reg'),
    # url(r'^other_reg/$',  'other_reg', name='other_reg'),
    url(r'^about_us/$',  'about_us', name='about_us'),
    url(r'^contact_us/$',  'contact_us', name='contact_us'),
    url(r'^disclaimer/$',  'disclaimer', name='disclaimer'),
    url(r'^checkvcode/$',  'checkvcode', name='checkvcode'),
    url(r'^activearea/$',  'activearea', name='activearea'),
    url(r'^agreement/$',  'agreement', name='agreement'),

     url(r'^checkuser/$',  'checkuser', name='checkuser'),
    url(r'^checkuser_phone/$',  'checkuser_phone', name='checkuser_phone'),
    url(r'^user_updatepwd/$',  'user_updatepwd', name='user_updatepwd'),
    url(r'^phone_infoPage/$',  'phone_infoPage', name='phone_infoPage'),
    url(r'^send_smscode/$',  'send_smscode', name='send_smscode'),
    url(r'^checksmscode/$',  'checksmscode', name='checksmscode'),
    url(r'^safecenter/$',  'safecenter', name='safecenter'),
    url(r'^change_phone_number/$',  'change_phone_number', name='change_phone_number'),
    url(r'^send_smscode_modify/$',  'send_smscode_modify', name='send_smscode_modify'),

)


urlpatterns += patterns('searcher.viewss',
    url(r'^qq_is_first/$',  'qq_is_first', name='qq_is_first'),
    url(r'^wb_is_first/$',  'wb_is_first', name='wb_is_first'),
    url(r'^wx_is_first/$',  'wx_is_first', name='wx_is_first'),
    url(r'^wxcheck/$',  'wxcheck', name='wxcheck'),
    url(r'^wx_binding/$',  'wx_binding', name='wx_binding'),
    url(r'^wx_register/$',  'wx_register', name='wx_register'),
    url(r'^ch_access_token/$',  'ch_access_token', name='ch_access_token'),
    url(r'^test_thread/$',  'remind_thread', name='remind_thread'),
    url(r'^test_thread_on/$',  'test_thread_on', name='test_thread_on'),
    url(r'^send_message/$',  'send_message', name='send_message'),
    url(r'^wx_bid_detail/(?P<objectid>\d+)/$',  'wx_bid_detail', name='wx_bid_detail'),
)

urlpatterns += patterns('searcher.views_m',
    url(r'^m/contact/$', 'contact', name='contact_m'),
    url(r'^m/$', 'index', name='index_m'),
    url(r'^m/search/$', 'search', name='search_m'),
    url(r'^m/search_result/$', 'search_result', name='search_result_m'),
    url(r'^m/search_listresult/$', 'search_listresult', name='search_listresult_m'),
    url(r'^m/result/$', 'result', name='result_m'),
    url(r'^m/login/$',  'login', name='login_m'),
    url(r'^m/logout/$',  'logout', name='logout_m'),
    url(r'^m/register/$',  'register', name='register_m'),
    url(r'^m/forgetpw/$',  'forgetpw', name='forgetpw_m'),
    url(r'^m/bid_detail/(?P<objectid>\d+)/$',  'bid_detail', name='bid_detail_m'),
    url(r'^m/bid_detail_p/$',  'bid_detail_p', name='bid_detail_p_m'),
    url(r'^m/agreement/$',  'agreement', name='agreement_m'),
)