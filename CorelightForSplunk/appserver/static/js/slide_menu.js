require.config({"paths":{"react":"/static/app/CorelightForSplunk/js/react.js?v=58b0ab0c732ebef71a93","react-dom":"/static/app/CorelightForSplunk/js/react-dom.js?v=4dd83184cfdcc08bae73"},"shim":{"react":{"exports":"react"},"react-dom":{"exports":"react-dom"}}});
                require([
                        "splunkjs/ready!",
                        "splunkjs/mvc/simplexml/ready!",
                        "splunkjs/mvc/utils",
                        "react", "react-dom", "jquery"
                    ], function (mvc,
                                 ignored,
                                 splunkjsUtils,
                                 react, reactdom, jQuery
                    ) {
                        let mySelf = document.getElementById("navSkip");
                        reactdom.render(
                            react.createElement(SlideMenu.default, {
                                splunkjs: mvc,
                                utils: splunkjsUtils,
                                splunk_components: { jQuery: jQuery, },
                                mySelf: mySelf.cloneNode(true)
                                }),
                            mySelf
                            );
                    });
                