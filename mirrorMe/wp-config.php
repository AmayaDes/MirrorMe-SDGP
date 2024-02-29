<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'mirrormeDB' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'qG4|-x$&J[W91c7LY!p3WPK QvzR`My-LLe2GTLG+#6{>jtJL:wC1oX<I+-bit2W' );
define( 'SECURE_AUTH_KEY',  '=>2xh6++TL6SxhB5B!q(E1ByCXJ([5T~6#LhA^jKD-WI3;bfy]ekdNG#Gy-/(~~E' );
define( 'LOGGED_IN_KEY',    'j Je;e.#Q$ pBAI.hqh)V*dP:Q@ht]avOl3FQQq3qvEBt1R>V07)Jby6]#W4(Lb_' );
define( 'NONCE_KEY',        'UOJC<LzDy`r}{;o^#59HFjWp*,8Q>u&xErLjVdiCMdclx5riI<.AecRo.zk>.LdU' );
define( 'AUTH_SALT',        'Ij+;lHO1{UH@9J`gz<|{A]T2iq!OZK^:Zyn=|z)$<oIFLH70q_}7xLpzEqLk=cdX' );
define( 'SECURE_AUTH_SALT', 'YTLU]m#s3@2^U?DpM=;|VL{Y(am^D{W*P@LWnUmjI<R<W4&f8(ugUzEP_Y$zOuU[' );
define( 'LOGGED_IN_SALT',   '2^cT~d&qJ2[o>(>,TQmI?A%K}LM1{RTU*t+F@he%t{52`0S9KX&%H~O8~k_:1}M#' );
define( 'NONCE_SALT',       '|1,Fg)={&SYa(E)N9Q]U/B)z(?#i#lSI:D$]>9!SQ1-tf`Av0}M7RFU?/Y<_s^/G' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
