const path = require('path');
const {
    series,
    watch,
    src,
    dest,
} = require('gulp');
const terser = require('gulp-terser-js')
const uglifycss = require('gulp-uglifycss');
const purgecss = require('gulp-purgecss')
const rename = require('gulp-rename');
const babel = require('gulp-babel');
const sass = require('gulp-sass');
const webpack = require('webpack-stream');

const BASE_DIR = __dirname


function buildJS() {
    return src(path.join(BASE_DIR, 'static/js/*.js'))
        .pipe(babel())
        // @ts-ignore
        .pipe(webpack(require('./webpack.config.js')))
        .pipe(terser({
            mangle: {
                toplevel: true
            }
        }))
        .pipe(rename({
            extname: '.min.js'
        }))
        .pipe(dest(path.join(BASE_DIR, 'static/dist/js')))
}

function buildSass() {
    return src(path.join(BASE_DIR, 'static/sass/*.scss'))
        .pipe(sass().on('error', sass.logError))
        .pipe(uglifycss({
            "maxLineLen": 80,
            "uglyComments": true
        }))
        // @ts-ignore
        // .pipe(purgecss({
        //     content:['templates/base.html', "blog/templates/blog/post_list.html", "blog/templates/blog/post_detail.html"]
        // }))
        .pipe(rename({
            extname: '.min.css'
        }))
        .pipe(dest(path.join(BASE_DIR, 'static/dist/css')))

}

exports.default = series(buildJS, buildSass);
exports.dev = function () {
    watch('static/sass/*.scss', buildSass);
    watch('static/js/*.js', buildJS);
}
