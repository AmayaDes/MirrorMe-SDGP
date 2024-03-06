<?php
/**
 *
 * @package           MirrorMe
 * @author            SDGP CS-114
 *
 * @woocommerce-plugin
 * Plugin Name:       MirrorMe
 * Plugin URI:        https://example.com/plugin-name
 * Description:       Virtual try-on 
 * Version:           1.0.0
 * Requires at least: 5.2
 * Requires PHP:      7.2
 * Author:            SDGP CS-114
 * Author URI:        https://example.com
 */

 // Test to see if WooCommerce is active (including network activated).
$plugin_path = trailingslashit( WP_PLUGIN_DIR ) . 'woocommerce/woocommerce.php';

if (
    in_array( $plugin_path, wp_get_active_and_valid_plugins() )
    || in_array( $plugin_path, wp_get_active_network_plugins() )
) {

    // Schedule the event on plugin activation
    register_activation_hook( __FILE__, 'schedule_weekly_apparel_check' );

    function schedule_weekly_apparel_check() {
        // Schedule the event to run weekly
        if ( ! wp_next_scheduled( 'weekly_apparel_check' ) ) {
            wp_schedule_event( time(), 'weekly', 'weekly_apparel_check' );
        }
    }

    // Hook the event to the apparel check function
    add_action( 'weekly_apparel_check', 'check_apparel_products_weekly' );

    function check_apparel_products_weekly() {
        // Query WooCommerce products
        $args = array(
            'post_type'      => 'product',
            'posts_per_page' => -1,
        );
        $products = new WP_Query( $args );
        // Array to store product images for apparel products
        $apparel_product_images = array();
        // Check if any products are apparel
        if ( $products->have_posts() ) {
            while ( $products->have_posts() ) {
                $products->the_post();
                // Check if the product belongs to the "Apparel" category or has specific attributes indicating it's apparel
                if ( has_term( 'apparel', 'product_cat' ) || has_term( 'apparel', 'product_attribute' ) ) {
                    // Get product image URL
                    $product_image_url = get_the_post_thumbnail_url( get_the_ID(), 'full' );
                    // Add product image URL to the array
                    $apparel_product_images[] = $product_image_url;
                }
            }
            wp_reset_postdata();
        }

    // Output result
    //add code here to send the images to model to create 3D models
    
}
add_action( 'woocommerce_single_product_summary', 'add_custom_button_to_product_page', 25 );

function add_custom_button_to_product_page(){
    // Output your custom button HTML with a link
    echo '<a href="https://amayades.github.io/Html/" class="custom-button" target="_blank">Try-On</a>';
    
    // You can style the button using CSS
    ?>
    <style>
    .custom-button {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        text-decoration: none;
    }
    </style>
    <?php
}
}
