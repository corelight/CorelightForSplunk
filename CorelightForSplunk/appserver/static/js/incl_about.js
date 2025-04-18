require.config({"paths":{"react-dom":"/static/app/CorelightForSplunk/js/react-dom.js?v=b7f55d1db31dd70953c6","about":"/static/app/CorelightForSplunk/js/about.js?v=c0e6d61bd0eeb3793c53","react":"/static/app/CorelightForSplunk/js/react.js?v=41a98d5155f771074e3e"},"shim":{"react-dom":{"exports":"react-dom"},"about":{"exports":["about"]},"react":{"exports":"react"}}});
                require([
                        "splunkjs/ready!",
                        "splunkjs/mvc/simplexml/ready!",
                        "splunkjs/mvc/utils",
                        "react-dom", "about", "react"
                    ], function (mvc,
                                 ignored,
                                 splunkjsUtils,
                                 reactdom, about, react
                    ) {
                        let default_tokens = mvc.Components.get("default"), submitted_tokens = mvc.Components.get("submitted");
                        let splunk_theme_name = window.__splunk_page_theme__ ? window.__splunk_page_theme__ : window.DASHBOARD_THEME ? window.DASHBOARD_THEME : "default";
                        let myObjects = $("#root").each((k, v)=>{
                            const root = reactdom.createRoot(
                                v, 
                                {identifierPrefix: "about"});
                            const react_app = react.createElement(about.default, {
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
                