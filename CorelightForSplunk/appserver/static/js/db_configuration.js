require.config({"paths":{"configuration":"/static/app/CorelightForSplunk/js/configuration.js?v=765b42e330b08b043ea4","react":"/static/app/CorelightForSplunk/js/react.js?v=58b0ab0c732ebef71a93","react-dom":"/static/app/CorelightForSplunk/js/react-dom.js?v=4dd83184cfdcc08bae73"},"shim":{"configuration":{"exports":["configuration"]},"react":{"exports":"react"},"react-dom":{"exports":"react-dom"}}});
                require([
                        "splunkjs/ready!",
                        "splunkjs/mvc/simplexml/ready!",
                        "splunkjs/mvc/utils",
                        "configuration", "react", "react-dom", "jquery"
                    ], function (mvc,
                                 ignored,
                                 splunkjsUtils,
                                 configuration, react, reactdom, jQuery
                    ) {
                        let mySelf = document.getElementById("root");
                        reactdom.render(
                            react.createElement(configuration.default, {
                                splunkjs: mvc,
                                utils: splunkjsUtils,
                                splunk_components: { jQuery: jQuery, },
                                mySelf: mySelf.cloneNode(true)
                                }),
                            mySelf
                            );
                    });
                