require.config({"paths":{"DashboardTabs":"/static/app/CorelightForSplunk/js/DashboardTabs.js?v=eb7a633dd9667e7b796c","react":"/static/app/CorelightForSplunk/js/react.js?v=58b0ab0c732ebef71a93","react-dom":"/static/app/CorelightForSplunk/js/react-dom.js?v=4dd83184cfdcc08bae73"},"shim":{"DashboardTabs":{"exports":["DashboardTabs"]},"react":{"exports":"react"},"react-dom":{"exports":"react-dom"}}});
                require([
                        "splunkjs/ready!",
                        "splunkjs/mvc/simplexml/ready!",
                        "splunkjs/mvc/utils",
                        "DashboardTabs", "react", "react-dom", "jquery"
                    ], function (mvc,
                                 ignored,
                                 splunkjsUtils,
                                 DashboardTabs, react, reactdom, jQuery
                    ) {
                       let myObjects = jQuery(".tab_root").each((k, v)=>{
                            reactdom.render(
                            react.createElement(DashboardTabs.default, {
                                splunkjs: mvc,
                                splunk_components: { jQuery: jQuery, } ,
                                jQuery: jQuery,
                                ...jQuery(v).data()
                                }),
                             v
                            );
                        });
                    });
                