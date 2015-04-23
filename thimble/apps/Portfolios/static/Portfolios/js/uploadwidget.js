! function(e) {
    "use strict";
    "function" == typeof define && define.amd ? define([], e) : e()
}(function() {
    "use strict";
    var e, t, i = 0,
        n = window.location.search.indexOf("debug=true") > -1;
    window.jQuery ? t = window.jQuery : window.$ && window.$.fn && window.$.fn.jquery && (t = window.$);
    var a = function(e) {
            if (null == e || "object" != typeof e || e.tagName) return e;
            var t = e.constructor();
            for (var i in e) t[i] = a(e[i]);
            return t
        },
        o = function(e, t) {
            return t = a(t), t.kind = e, JSON.stringify(t)
        },
        d = function(e) {
            return JSON.parse(e)
        },
        r = function() {
            try {
                var e = document.createElement("style");
                e.type = "text/css", e.innerHTML = ".cloudinary-thumbnails { list-style: none; margin: 10px 0; padding: 0 } .cloudinary-thumbnails:after { clear: both; display: block; content: '' } .cloudinary-thumbnail { float: left; padding: 0; margin: 0 15px 5px 0; display: none } .cloudinary-thumbnail.active { display: block } .cloudinary-thumbnail img { border: 1px solid #01304d; border-radius: 2px; -moz-border-radius: 2px; -webkit-border-radius: 2px } .cloudinary-thumbnail span { font-size: 11px; font-family: Arial, sans-serif; line-height: 14px; border: 1px solid #aaa; max-width: 150px; word-wrap: break-word; word-break: break-all; display: inline-block; padding: 3px; max-height: 60px; overflow: hidden; color: #999; } .cloudinary-delete { vertical-align: top; font-size: 13px; text-decoration: none; padding-left: 2px; line-height: 8px; font-family: Arial, sans-serif; color: #01304d }.cloudinary-button { color: #fefeff; text-decoration: none; font-size: 18px; line-height: 28px; height: 28x; border-radius: 6px; -moz-border-radius: 6px; -webkit-border-radius: 6px; font-weight: normal; text-decoration: none;   display: inline-block; padding: 4px 30px 4px 30px; background: #0284cf; font-family: Helvetica, Arial, sans-serif;   background: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgdmlld0JveD0iMCAwIDEgMSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+CiAgPGxpbmVhckdyYWRpZW50IGlkPSJncmFkLXVjZ2ctZ2VuZXJhdGVkIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzAyODRjZiIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwMjU5OGIiIHN0b3Atb3BhY2l0eT0iMSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEiIGhlaWdodD0iMSIgZmlsbD0idXJsKCNncmFkLXVjZ2ctZ2VuZXJhdGVkKSIgLz4KPC9zdmc+);   background: -moz-linear-gradient(top,  #0284cf 0%, #02598b 100%);   background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#0284cf), color-stop(100%,#02598b));   background: -webkit-linear-gradient(top,  #0284cf 0%,#02598b 100%);   background: -o-linear-gradient(top,  #0284cf 0%,#02598b 100%);   background: -ms-linear-gradient(top,  #0284cf 0%,#02598b 100%);   background: linear-gradient(to bottom,  #0284cf 0%,#02598b 100%);   filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#0284cf', endColorstr='#02598b',GradientType=0 ); }.cloudinary-button:hover { background: #02598b;   background: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgdmlld0JveD0iMCAwIDEgMSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+CiAgPGxpbmVhckdyYWRpZW50IGlkPSJncmFkLXVjZ2ctZ2VuZXJhdGVkIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzAyNTk4YiIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwMjg0Y2YiIHN0b3Atb3BhY2l0eT0iMSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEiIGhlaWdodD0iMSIgZmlsbD0idXJsKCNncmFkLXVjZ2ctZ2VuZXJhdGVkKSIgLz4KPC9zdmc+);   background: -moz-linear-gradient(top,  #02598b 0%, #0284cf 100%);   background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#02598b), color-stop(100%,#0284cf));   background: -webkit-linear-gradient(top,  #02598b 0%,#0284cf 100%);   background: -o-linear-gradient(top,  #02598b 0%,#0284cf 100%);   background: -ms-linear-gradient(top,  #02598b 0%,#0284cf 100%);   background: linear-gradient(to bottom,  #02598b 0%,#0284cf 100%);   filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#02598b', endColorstr='#0284cf',GradientType=0 ); ";
                var t = document.getElementsByTagName("head")[0];
                t && t.appendChild(e)
            } catch (i) {
                console && console.log && console.log("Cannot initialize stylesheet: " + i)
            }
        };
    r();
    var l = function(r, l) {
            var c, u, s, g = i++,
                p = a(r),
                b = p.element,
                f = !1,
                m = !1;
            delete p.element, p.widget_id = g;
            var y = function() {
                    p.cloud_name || (p.cloud_name = e), p.secure = p.secure || "https:" === document.location.protocol;
                    for (var t = ["cloud_name", "upload_preset"], i = 0; i < t.length; i++)
                        if (!p[t[i]]) throw "Missing required option: " + t[i];
                    c = window.document.createElement("iframe");
                    var a = p.secure ? "https:" : "http:",
                        d = n ? "?debug=true" : "";
                    s = p.widgetHost || a + "//widget.cloudinary.com", c.setAttribute("src", s + "/v/" + p.cloud_name + "/4c0ba727430383bc0b140524cddf6025/all" + d), c.setAttribute("width", "100%"), c.setAttribute("height", "100%"), c.setAttribute("frameborder", "no"), c.setAttribute("style", "position: fixed; top: 0; left: 0; background: transparent; z-index: 1000000"), c.style.display = "none", h(c, "load", function() {
                        c.contentWindow.postMessage(o("init", p), s), m = !0, f && (c.style.display = "block", c.focus(), c.contentWindow.postMessage(o("open", {}), s))
                    }), h(window, "message", v), window.document.body.appendChild(c), h(window.document, "keyup", function(e) {
                        27 == e.keyCode && k()
                    }), b && w()
                },
                w = function() {
                    b.style.display = "none";
                    var e = window.document.createElement("a");
                    e.setAttribute("class", p.button_class || "cloudinary-button"), e.setAttribute("href", "#"), e.innerHTML = p.button_caption || "Upload image", b.parentNode.insertBefore(e, b.previousSibling), h(e, "click", function(e) {
                        return I(), e && e.preventDefault && e.preventDefault(), e && e.stopPropagation && e.stopPropagation(), !1
                    }), !p.field_name && b.getAttribute("name") && "" != b.getAttribute("name") && (p.field_name = b.getAttribute("name"))
                },
                h = function(e, t, i) {
                    e.addEventListener ? e.addEventListener(t, i, !1) : e.attachEvent("on" + t, i)
                },
                I = function() {
                    f = !0, u = window.document.body.style.overflow, window.document.body.style.overflow = "hidden", m && (c.style.display = "block", c.focus(), c.contentWindow.postMessage(o("open", {}), s))
                },
                v = function(e) {
                    if (e.origin.match(/cloudinary\.com/)) {
                        var i;
                        try {
                            i = d(e.data)
                        } catch (n) {
                            return
                        }
                        if (i.widget_id == g) switch (i.kind) {
                            case "success":
                                p.keep_widget_open || k(), C(i.result), l && l(null, i.result), t && t(b || p.form || document).trigger("cloudinarywidgetsuccess", [i.result]);
                                break;
                            case "error":
                                k(), l && l(i), t && t(b || p.form || document).trigger("cloudinarywidgeterror", i);
                                break;
                            case "closed":
                                k();
                                var a = {
                                    message: "User closed widget"
                                };
                                l && l(a), t && t(b || p.form || document).trigger("cloudinarywidgetclosed", a)
                        }
                    }
                },
                k = function() {
                    c.style.display = "none", window.document.body.style.overflow = u, f = !1
                },
                C = function(e) {

                    if (t) {
                        var i = p.form;
                        !i && i !== !1 && b && (i = t(b).parents("form")[0]);


                        var n = p.field_name || "image";
                        if (i && t.each(e, function(e, a) {
                                var o, d = [a.resource_type, a.type, a.path].join("/") + "#" + a.signature,
                                    r = function() {
                                        var e = t("<input></input>").attr({
                                            type: "hidden",
                                            name: n
                                        }).val(d).addClass("cloudinary-hidden-field").attr("data-cloudinary-public-id", a.public_id).appendTo(i);
                                        t(e).data("cloudinary", a)
                                    };

                                // DEVIATION FROM SOURCE to allow multiple entry photos:
                                if(n=="cover_photo" || n=='avatar'){
                                   o = b && "input" == b.tagName && "hidden" == t(b).attr("type") ? t(b) : t(i).find('input[name="' + n + '"]'), 0 == e && o.length > 0 ? (o.val(d), o.attr("data-cloudinary-public-id", a.public_id), o.data("cloudinary", a), o.addClass("cloudinary-hidden-field")) : r()
                                }
                                else{
                                   r();
                                }
                            }),



                            p.thumbnails !== !1 && (p.thumbnails || b)) {
                                // DEVIATION FROM SOURCE to only show one cover thumbnail:
                                if(p.field_name == "cover_photo"){
                                  $(".cloudinary-thumbnails .cover_photo").remove();
                                }
                                if(p.field_name == "avatar"){
                                  $(".cloudinary-thumbnails .avatar").remove();
                                }
                                var a = t("<ul></ul>").addClass("cloudinary-thumbnails");
                                t.each(e, function(e, i) {
                                    var n = t("<li></li>").addClass("cloudinary-thumbnail " + p.field_name).data("cloudinary", i);
                                    n.append(i.thumbnail_url ? t("<img></img>").attr("src", i.thumbnail_url) : t("<span></span>").text(i.public_id)), i.delete_token && n.append(t("<a></a>").addClass("cloudinary-delete").attr("href", "#").text("\xd7")), n.find("img").on("load", function() {
                                        n.addClass("active")
                                    }), a.append(n)
                                }), a.find("li").length > 0 && (p.thumbnails ? t(p.thumbnails).append(a) : t(b).after(a)),
                                    a.find(".cloudinary-delete").click(function(e) {
                                    e.preventDefault();
                                    var a = t(this).parents(".cloudinary-thumbnail").data("cloudinary");
                                    if (x(a.delete_token), t(this).parents(".cloudinary-thumbnail").hide("slow"), i) {
                                        var o = t(i).find('input[name="' + n + '"][data-cloudinary-public-id="' + a.public_id + '"].cloudinary-hidden-field');
                                        t(i).find('input[name="' + n + '"].cloudinary-hidden-field').length > 1 ? t(o).remove() : t(o).attr("data-cloudinary-public-id", "").val("").data("cloudinary", null)
                                    }
                                })
                            }
                    }
                },
                x = function(e, i) {
                    if (t) {
                        i = i || {};
                        var n = i.url;
                        n || (n = "https://api.cloudinary.com/v1_1/" + p.cloud_name + "/delete_by_token");
                        var a = t.support.xhrFileUpload ? "json" : "iframe json";
                        return t.ajax({
                            url: n,
                            method: "POST",
                            data: {
                                token: e
                            },
                            headers: {
                                "X-Requested-With": "XMLHttpRequest"
                            },
                            dataType: a
                        })
                    }
                };
            return y(), {
                open: function() {
                    return I(), this
                },
                close: k
            }
        },
        c = {
            openUploadWidget: function(e, t) {
                return l(e, t).open()
            },
            createUploadWidget: function(e, t) {
                return l(e, t)
            },
            applyUploadWidget: function(e, t, i) {
                var n = a(t);
                return n.element = e, l(n, i)
            },
            setCloudName: function(t) {
                e = t
            }
        };
    window.cloudinary = c, t && (t.fn.cloudinary_upload_widget = function(e, i) {
        window.cloudinary.applyUploadWidget(t(this)[0], e, i)
    })
});