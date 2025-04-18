require.config({"paths":{"configuration":"/static/app/CorelightForSplunk/js/configuration.js?v=8531ef8fdb42f455aa38","react-dom":"/static/app/CorelightForSplunk/js/react-dom.js?v=b7f55d1db31dd70953c6","react":"/static/app/CorelightForSplunk/js/react.js?v=41a98d5155f771074e3e"},"shim":{"configuration":{"exports":["configuration"]},"react-dom":{"exports":"react-dom"},"react":{"exports":"react"}}});
                require([
                        "splunkjs/ready!",
                        "splunkjs/mvc/simplexml/ready!",
                        "splunkjs/mvc/utils",
                        "configuration", "react-dom", "react"
                    ], function (mvc,
                                 ignored,
                                 splunkjsUtils,
                                 configuration, reactdom, react
                    ) {
                        let default_tokens = mvc.Components.get("default"), submitted_tokens = mvc.Components.get("submitted");
                        let splunk_theme_name = window.__splunk_page_theme__ ? window.__splunk_page_theme__ : window.DASHBOARD_THEME ? window.DASHBOARD_THEME : "default";
                        let myObjects = $("#root").each((k, v)=>{
                            const root = reactdom.createRoot(
                                v, 
                                {identifierPrefix: "configuration"});
                            const react_app = react.createElement(configuration.default, {
                                    splunkjs: mvc,
                                    mvc: mvc,
                                    utils: splunkjsUtils,
                                    app_context: "CorelightForSplunk",
                                    family: splunk_theme_name,
                                    color_scheme: splunk_theme_name,
                                    ...$(v).data(),
                                    default_tokens, submitted_tokens,
                                    
                                    });
                            
                            root.render(react_app);
                          }); //end iterator
                       });
                